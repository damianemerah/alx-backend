import { createClient } from 'redis';

const client = createClient();

client.on('err', err => console.log('Redis client not connected to the server:', err.toString()));
client.on('ready', () => console.log('Redis client connected to the server'));

