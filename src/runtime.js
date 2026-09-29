import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
const ROOT=dirname(dirname(fileURLToPath(import.meta.url)));
function localScan(text) {
  return spawnSync("python3",[join(ROOT,"scripts","sanitize.py"),"--strict","--silent","--report"],{input:text,encoding:"utf8",timeout:25000,maxBuffer:1024*1024});
}
export function createClawDefenderRuntime(config={},logger={},runner=localScan) {
  const maxChars=config.maxChars ?? 2_000_000;
  function beforeAgentRun(event) {
    const prompt=String(event?.prompt ?? "");
    if (!prompt) return {outcome:"pass"};
    if (prompt.length>maxChars) return {outcome:"block",reason:"input exceeds configured passive scan limit",message:config.blockedMessage ?? "Input terlalu besar untuk diperiksa dengan aman.",category:"untrusted-input-unscanned"};
    try {
      const result=runner(prompt);
      if (result?.status===0) return {outcome:"pass"};
      if (result?.status===1) return {outcome:"block",reason:"local scanner detected suspicious input",message:config.blockedMessage ?? "Input ditolak oleh pemeriksaan keamanan. Periksa atau kirim ulang tanpa instruksi mencurigakan.",category:"untrusted-input"};
      logger.warn?.("clawdefender: passive scanner unavailable; blocked fail-closed");
      return {outcome:"block",reason:"local scanner unavailable or invalid",message:"Input belum dapat diperiksa dengan aman. Coba lagi setelah pemeriksa tersedia.",category:"untrusted-input-unscanned"};
    } catch {
      logger.warn?.("clawdefender: passive scanner threw; blocked fail-closed");
      return {outcome:"block",reason:"local scanner threw",message:"Input belum dapat diperiksa dengan aman. Coba lagi setelah pemeriksa tersedia.",category:"untrusted-input-unscanned"};
    }
  }
  return {beforeAgentRun};
}
