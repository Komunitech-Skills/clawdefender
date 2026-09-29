import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";
import { createClawDefenderRuntime } from "./src/runtime.js";
export default definePluginEntry({
  id: "clawdefender",
  name: "ClawDefender",
  description: "Fail-closed preflight for the user input that is about to start an agent run.",
  register(api) {
    const runtime=createClawDefenderRuntime(api.pluginConfig ?? {}, api.logger);
    api.on("before_agent_run", runtime.beforeAgentRun, {priority: 100});
  },
});
