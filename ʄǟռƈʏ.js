// ⬡ ™𝐊𝐫𝐚𝐤𝐢𝐧𝐳 ⬡==========================⬡    🍁 (c)Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡ 𝐋𝐚𝐛™ ⬡
const fs = require(`fs`);
const Kolor = require(`chalk`);
const ascii = require(`ascii-table`);
const ᴍɪᴢᴜᴋɪᴛᴀʙʟᴇ = new ascii().setHeading(
  `🍁𝐂𝐨𝐦𝐦𝐚𝐧d 𝐍𝐚𝐦𝐞🍁`,
  `🍁𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗙𝗼𝗹𝗱𝗲𝗿🍁`,
  `🍁𝐇𝐞𝐚𝐥𝐭𝐡🍁`
);
// ⬡ ™𝐊𝐫𝐚𝐤𝐢𝐧𝐳 ⬡==========================⬡    🍁 (c)Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡ 𝐋𝐚𝐛™ ⬡
function ʄǟռƈʏ(ꜱɪᴛʀᴀᴘ, commandUsage) {
  const ᴍɪᴢᴜᴋɪᴅᴇʀꜱ = fs.readdirSync(`./Sasuke_linker`);
  for (const ʜᴏʟᴅᴇʀ of ᴍɪᴢᴜᴋɪᴅᴇʀꜱ) {
    const commandFiles = fs
      .readdirSync(`./Sasuke_linker/${ʜᴏʟᴅᴇʀ}`)
      .filter((ᴍɪꜱᴏ) => ᴍɪꜱᴏ.endsWith(`.js`));
    for (const ᴍɪꜱᴏ of commandFiles) {
      const command = require(`./Sasuke_linker/${ʜᴏʟᴅᴇʀ}/${ᴍɪꜱᴏ}`);
      ꜱɪᴛʀᴀᴘ.set(command.name, command);
      commandUsage.set(command.𝓜𝓮𝓮6ʍօʀɛ, command.description);
      try {
        ᴍɪᴢᴜᴋɪᴛᴀʙʟᴇ.addRow(
          Kolor.green.italic(command.name.toUpperCase()),
          ʜᴏʟᴅᴇʀ,
          `✔️   𝘚𝘺𝘮-𝘓𝘪𝘯𝘬𝘦𝘥`
        );
      } catch {
        ᴍɪᴢᴜᴋɪᴛᴀʙʟᴇ.addRow(
          Kolor.green.italic(command.name),
          ʜᴏʟᴅᴇʀ,
          `✔️   𝘚𝘺𝘮-𝘓𝘪𝘯𝘬𝘦𝘥`
        );
      }
    }
    console.log(ᴍɪᴢᴜᴋɪᴛᴀʙʟᴇ.toString());
  }
  // const spawn = require("child_process").spawn;
  // spawn("python", ["path/to/script.py"]);
}
module.exports = { ʄǟռƈʏ };
// ⬡ ™𝐊𝐫𝐚𝐤𝐢𝐧𝐳 ⬡==========================⬡    🍁 (c)Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡ 𝐋𝐚𝐛™ ⬡
