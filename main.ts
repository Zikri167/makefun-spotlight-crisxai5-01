// Copies POST.json from the bot directory into the output directory.
// That is the program's only job: nothing else is read or written.
import { copyFile, mkdir, readFile } from "node:fs/promises";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

// Read the file first so a malformed POST.json fails loudly here,
// before anything is copied to the output directory.
const postPath = join(botDir, "POST.json");
const raw = await readFile(postPath, "utf8");
const parsed: unknown = JSON.parse(raw);
if (
  typeof parsed !== "object" ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== "string"
) {
  throw new Error("POST.json must be a JSON object with a string url field");
}

try {
  await mkdir(outDir, { recursive: true });
  await copyFile(postPath, join(outDir, "POST.json"));
} catch (err) {
  console.error(err);
  process.exit(1);
}
