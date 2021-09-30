const fs = require('fs');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const { execute } = require('./events/ready');
const config = require('../env/config/config.json')


module.exports = {
    execute(client) {
        const commands = [];
        const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

        const clientId = client.application.id;
        const guildId = client.guilds.cache.map(guild => guild.id);

        for (const file of commandFiles) {
            const command = require(`./commands/${file}`);
            commands.push(command.data.toJSON());
        }

        const rest = new REST({ version: '9' }).setToken(config.token);

        for (let guilds of guildId) {
            (async () => {
                try {
                    console.log(`Started refreshing application (/) commands for: ${client.guilds.cache.find(guild => guild.id === guilds).name}`);

                    await rest.put(
                        Routes.applicationGuildCommands(clientId, guilds),
                        { body: commands },
                    );

                    console.log('Successfully reloaded application (/) commands.');
                } catch (error) {
                    console.error(error);
                }

            })();
        }
    }
}