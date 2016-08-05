'use strict'

const http = require("http");

let options = {
  "method": "GET",
  "hostname": "httpbin.org",
  "path": "/ip"
};

let req = http.request(options, function (res) {
  let chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    let body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.end();
