// Local preview: node server.js  ->  http://localhost:3000
const http=require('http'),fs=require('fs'),path=require('path');
const T={'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp','.ico':'image/x-icon','.xml':'application/xml','.txt':'text/plain','.webmanifest':'application/manifest+json'};
http.createServer((q,s)=>{let u=decodeURIComponent(q.url.split('?')[0]);if(u.endsWith('/'))u+='index.html';
const f=path.join(__dirname,u);if(!f.startsWith(__dirname))return s.end();
fs.readFile(f,(e,d)=>{if(e)return fs.readFile(path.join(__dirname,'404.html'),(_,n)=>{s.writeHead(404,{'Content-Type':T['.html']});s.end(n)});
s.writeHead(200,{'Content-Type':T[path.extname(f)]||'application/octet-stream'});s.end(d)})}).listen(process.env.PORT||3000);
