const { Client, Collection, Intents } = require('discord.js');
const Discord = require('discord.js')
const fs = require('fs');
let configJson = require('../env/config/config.json')

const client = new Client({ partials: [ "MESSAGE", "CHANNEL", "REACTION"], intents: [Intents.FLAGS.GUILDS]});

client.commands = new Discord.Collection();
client.events = new Discord.Collection();

['command_handler', 'event_handler'].forEach(handler => {
    require(`./handlers/${handler}`)(client, Discord);
})

client.login(configJson.token);