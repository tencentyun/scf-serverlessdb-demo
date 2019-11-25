'use strict';
// node.js demo
const database = require('scf-nodejs-serverlessdb-sdk').database;

exports.main_handler = async (event, context, callback) => {
  let connection = await database().connection();
  let result = await connection.queryAsync('select * from name');
  console.log(result);
}
