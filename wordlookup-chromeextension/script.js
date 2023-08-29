async function fetchData() {
    const res=await fetch ("https://$GCP_REGION-$GCP_PROJECT.cloudfunctions.net/wotd");
    const record=await res.json();
    document.getElementById("wotd").innerHTML=record.wotd[0].details;
}
fetchData();