module.exports = (Discord, client, message) => {
    const prefix = require ('../../env/config/config.json');
    if (!message.content.startsWith(prefix.prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.prefix.length).split(/ +/);
    const cmd = args.shift().toLowerCase();

    const command = client.commands.get(cmd);

    if(command) command.execute(client, message, args, Discord);
}