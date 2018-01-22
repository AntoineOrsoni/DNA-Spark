module.exports = function (controller) {

    controller.hears(["(.*)", "who"], 'direct_message,direct_mention', function (bot, message) {
        var name = message.match[1];
        var text = "I heard : ";
        text += name + " !";
        bot.reply(message, text);
    });
}