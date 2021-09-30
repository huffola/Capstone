const { Interaction } = require('discord.js');
const Sequelize = require('sequelize');

const localDB = new Sequelize('database', 'user', 'password', {
    host: 'localhost',
    dialect: 'sqlite',
    logging: false,
    sotrage: 'database.sqlite'
});

const myGuilds = localDB.define('myGuilds', {
    guildID: {
        type: Sequelize.INTEGER,
        unique: true
    },
    guildName: Sequelize.STRING,
    guildMembers: Sequelize.STRING
})

module.exports = {
    name: "ready",
    once: true,
    async execute(client) {
        myGuilds.sync();
        const guildIds = client.guilds.cache.map(guild => guild.id);
        for(const guild of guildIds){
            const list = client.guilds.cache.get(guild);
            console.log(list.members.cache.map(member => member.user.tag))
            // const myguilds = await myGuilds.create({
            //     guildID: guild,
            //     guildName: client.guilds.cache.find(guilds => guilds.id === guild).name,

            // })
        }
        const interactionCommands = require('../deploy-commands')
        interactionCommands.execute(client)
        console.log('\x1b[36m%s\x1b[0m', `Successfully logged in as ${client.user.tag}`);
    }
}