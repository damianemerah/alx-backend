import { createClient, print } from 'redis';

const client = createClient();

client.on('err', err => console.log('Redis client not connected to the server:', err.toString()));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (_, reply) => {
    console.log(reply);
  });
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}


client.on('connect', async () => await main())
