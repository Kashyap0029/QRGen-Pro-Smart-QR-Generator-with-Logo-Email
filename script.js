document.getElementById("qrForm").addEventListener("submit", async function(e){
e.preventDefault();
const url=document.getElementById("url").value;
const email=document.getElementById("email").value;
const logo=document.getElementById("logo").files[0];
const fd=new FormData();
fd.append("url",url);
fd.append("email",email);
if(logo) fd.append("logo",logo);
document.getElementById("status").innerText="Generating...";
const res=await fetch("http://127.0.0.1:8000/generate",{method:"POST",body:fd});
const data=await res.json();
document.getElementById("qrImage").src="data:image/png;base64,"+data.qr_image;
document.getElementById("status").innerText="Done!";
});