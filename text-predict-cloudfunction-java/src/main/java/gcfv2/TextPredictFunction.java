package gcfv2;

import java.io.BufferedWriter;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.stream.Collectors;

//Logging packages
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.cloud.functions.HttpFunction;
import com.google.cloud.functions.HttpRequest;
import com.google.cloud.functions.HttpResponse;

//LangChain4j packages
import dev.langchain4j.data.message.AiMessage;
import dev.langchain4j.data.message.UserMessage;
import dev.langchain4j.model.output.Response;
import dev.langchain4j.model.vertexai.VextexAiLanguageModel;

public class TextPredictFunction implements HttpFunction {
  
  private static Logger logger = LoggerFactory.getLogger(TextPredictFunction.class);

  public void service(final HttpRequest request, final HttpResponse response) throws Exception {
    final BufferedWriter writer = response.getWriter();

    //Read the environment variables which will be passed to the Vertex AI Model for initialization
    String GCP_REGION = System.getenv("GCP_REGION");
    String GCP_PROJECT = System.getenv("GCP_PROJECT");

    //Fetch the prompt from the JSON body in the request
    BufferedReader reader = new BufferedReader(new InputStreamReader(request.getInputStream()));
    String jsonRequest = reader.lines().collect(Collectors.joining());

    // Parse the JSON data
    Gson gson = new Gson();
    JsonObject jsonRequestObject = gson.fromJson(jsonRequest, JsonObject.class);

    // Get the data from the JSON object
    String prompt = jsonRequestObject.get("prompt").getAsString();
    if (prompt.length() > 0) {

      VextexAiLanguageModel vertexAiLanguageModel = VextexAiLanguageModel.builder()
          .endpoint("us-central1-aiplatform.googleapis.com:443")
          .project(GCP_PROJECT)
          .location(GCP_REGION)
          .publisher("google")
          .modelName("text-bison@001")
          .temperature(1.0)
          .maxOutputTokens(50)
          .topK(0)
          .topP(0.0)
          .maxRetries(3)
          .build();

      Response<String> modelResponse = vertexAiLanguageModel.generate(prompt);            
      logger.info("Result: " + modelResponse.content());
      writer.write(modelResponse.content());
    }
    else {
      logger.info("No prompt provided.");
      writer.write("No prompt provided.");
    }
  }
}
