module.exports = function (controller) {

    controller.hears(["Antoine", "who"], 'direct_message,direct_mention', function (bot, message) {
        var text = "I heard Antoine !";
        bot.reply(message, text);
    });
}