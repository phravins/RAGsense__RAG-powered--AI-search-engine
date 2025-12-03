const BACKEND = "https://RAGsense-abc123-4567.app.github.dev"; // <-- your Codespaces url

document.getElementById("ask").onclick = async () => {
  const [tab] = await chrome.tabs.query({active:true, currentWindow:true});
  const url = tab.url;
  const question = document.getElementById("question").value;
  document.getElementById("answer").textContent = "Thinking…";
  const res = await fetch(`${BACKEND}/ask`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({url, question})
  });
  const json = await res.json();
  document.getElementById("answer").textContent = json.answer;
};