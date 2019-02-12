'use strict';
const path 	= require('path');
const fs 	= require('fs');

var jwt 	= require('jsonwebtoken');

var priKey 	= fs.readFileSync('./private.key','utf8');
var pubKey	= fs.readFileSync('./public.key','utf8');


var payload = {'user_id': 'vietstar'};
var iss = "vietstar test app";
var sub = "huybinh@lampart-vn.com";
var aud = "http://lampart-vn.com";
var exp = "2h";

// var secret_Key = "vietstar thaihuybinh@lampart-vn.com";
var signOptions = {
	issuer		: iss,
	subject		: sub,
	audience	: aud,
	expiresIn	: exp,
	algorithm	: "HS256"
}

var token = jwt.sign(payload, pubKey /*secret_Key*/, signOptions);
console.log(token);

var verifyOptions = {
	issuer		: iss,
	subject		: sub,
	audience	: aud,
	maxAge		: exp,
	algorithm	: ["HS256"]
}
var decoded = jwt.decode(token, priKey /*secret_Key*/, verifyOptions);
console.log('Decode: ' + JSON.stringify(decoded,null,4));
