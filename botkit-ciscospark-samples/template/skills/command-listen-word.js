module.exports = function (controller) {

    controller.hears(["(.*)", "who"], 'direct_message,direct_mention', function (bot, message) {
        var name = message.match[1];
        var text = "I heard : ";
        text += name + " !";
        bot.reply(message, text);


        // Sending the POST

        var data = JSON.stringify({
            "ipAddress": name
        });

        var url = "http://127.0.0.1:5000";


        var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function () {
              if (this.readyState === 4) {
                console.log(this.responseText);
              }
        });

        xhr.open("POST", url);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("Cache-Control", "no-cache");

        xhr.send(data);
    });
}