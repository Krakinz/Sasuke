// ⬡ ™𝐊𝐫𝐚𝐤𝐢𝐧𝐳 ⬡==========================⬡  (c)  ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡ 𝐋𝐚𝐛™ ⬡
const fs = require(`fs`);
const { Sequelize } = require(`sequelize`);
if (fs.existsSync(`Sasuke_core.env`)) {
  require(`dotenv`).config({
    path: `./Sasuke_core.env`,
  });
} else {
  require(`dotenv`);
}
// ⬡ ™𝐊𝐫𝐚𝐤𝐢𝐧𝐳 ⬡==========================⬡   (c) ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡ 𝐋𝐚𝐛™ ⬡
const env = {
  Mee6: process.env.SASUKE === undefined ? `Null` : process.env.SASUKE,
  HEROKU_API:
    process.env.HEROKU_API === undefined ? `Null` : process.env.HEROKU_API,
  HEROKU_BOT_NAME:
    process.env.HEROKU_BOT_NAME === undefined
      ? `Null`
      : process.env.HEROKU_BOT_NAME,
  Krakinz: process.env.Krakinz === undefined ? `Null` : process.env.Krakinz,
  IMDB: `5e36f0db`,
  FOXTROT: `^[/]`,
  CCD: process.env.CCD === undefined ? `254` : process.env.CCD,
  OCR: `9ffb44def388957`,
  TEN: `0G2R8PTUGMRP`,
  ɴᴏᴛᴍᴇᴀᴅᴍɪɴ: `./Sasuke_core/𝓜𝖎𝖟𝖚ӄ𝖎NotMeAdmin.png`,
  ɴᴏᴛᴀᴅᴍɪɴ: `./Sasuke_core/𝓜𝖎𝖟𝖚ӄ𝖎MemErr.png`,
  WAPI: `6729ac2b2e2bb5c686ff427a2f06df92`,
  UPT: `https://i.postimg.cc/sDXbg5xF/image.png`,
  ERROR: `https://i.postimg.cc/sDPF83Mx/Mizuki-Error.png`,
  INVL: `https://i.postimg.cc/q7k5WK9Z/Mizuki-Invalid.png`,
  HASH: `https://chat.whatsapp.com/D9gPfFXQq2lGL77meDgd8h`,
  DEV: `254718241545,254768413736`,
  SASUKEQL: (process.env.SASUKEQL =
    process.env.SASUKEQL === undefined
      ? `./Sasuke_core/Sasuke_core.db`
      : process.env.SASUKEQL),
  POSTQL:
    process.env.SASUKEQL === `./Sasuke_core/Sasuke_core.db`
      ? new Sequelize({ dialect: `sqlite`, storage: process.env.SASUKEQL })
      : new Sequelize(process.env.SASUKEQL, {
          dialect: `postgres`,
          protocol: `postgres`,
          dialectOptions: { ssl: { require: true, rejectUnauthorized: false } },
        }),
  MEE: "https://i.postimg.cc/hGxvvFbJ/2.png",
  PRIVACY: process.env.PRIVACY === undefined ? `public` : process.env.PRIVACY,
};
module.exports = env;
// ⬡ ™𝐊𝐫𝐚𝐤𝐢𝐧𝐳 ⬡==========================⬡   (c) ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡ 𝐋𝐚𝐛™ ⬡
