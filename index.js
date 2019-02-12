'use strict';

const path 	= require('path');
const fs 	= require('fs');

var jwt 	= require('jsonwebtoken');

var priKey 	= fs.readFileSync('./private.key','utf8');
var pubKey	= fs.readFileSync('./public.key','utf8');

// console.log(priKey);
// console.log(pubKey);

var payload = { };

payload.field01 = "Data 01";
payload.field02 = "Data 02";
payload.field03 = "Data 03";

// console.log("payload: " + JSON.stringify(payload,null,4));

var iss = "vietstar test app";
var sub = "huybinh@lampart-vn.com";
var aud = "http://lampart-vn.com";

var exp = "2h";

var signOptions = {
	issuer		: iss,
	subject		: sub,
	audience	: aud,
	expiresIn	: exp,
	algorithm	: "RS256"
}
// console.log("Options: " + JSON.stringify(signOptions,null,4));
// 
// signature digital
var token = jwt.sign(payload, priKey, signOptions);
console.log("Token: " + token);


var verifyOptions = {
	issuer		: iss,
	subject		: sub,
	audience	: aud,
	maxAge		: exp,
	algorithm	: ["RS256"]
}
// verify for signature digital
var verified = jwt.verify(token, pubKey, verifyOptions);
console.log("Verified: " + JSON.stringify(verified,null,4));

var decoded = jwt.decode(token, {complete: true});
console.log("Header: " + JSON.stringify(decoded.header,null,4));
console.log("Data: " + JSON.stringify(decoded.payload,null,4));

process.exitcode = 1;