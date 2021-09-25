const { execute } = require("../events/ready");

module.exports = {
    async execute(time) {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve();
            }, time);
        });
    }
}