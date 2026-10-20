### Kate Macias
### Software Engineering 1
### Fall 2026

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Close Reader</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,500;1,7..72,700&family=Figtree:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Layout: one 760px reading column; passages set like a book page, UI chrome kept quiet; highlighter marks carry emphasis */
:root {
  --paper: #f4f6f9;
  --surface: #ffffff;
  --ink: #18202e;
  --muted: #586274;
  --rule: #d8dde6;
  --accent: #2545c4;
  --accent-ink: #ffffff;
  --hl: #f1e44c;
  --hl-ink: #18202e;
  --good: #1b7547;
  --good-bg: #e2f2e9;
  --bad: #ad311e;
  --bad-bg: #f8e5e1;
  --font-read: "Literata", Georgia, "Times New Roman", serif;
  --font-ui: "Figtree", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-data: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #10141b; --surface: #171d27; --ink: #e6eaf1; --muted: #9ba5b6; --rule: #283040;
    --accent: #8fa5ff; --accent-ink: #10141b; --hl: #d9cc3c; --hl-ink: #10141b;
    --good: #62cf95; --good-bg: #15301f; --bad: #ff8b74; --bad-bg: #3a1c17; color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #10141b; --surface: #171d27; --ink: #e6eaf1; --muted: #9ba5b6; --rule: #283040;
  --accent: #8fa5ff; --accent-ink: #10141b; --hl: #d9cc3c; --hl-ink: #10141b;
  --good: #62cf95; --good-bg: #15301f; --bad: #ff8b74; --bad-bg: #3a1c17; color-scheme: dark;
}

* { box-sizing: border-box; }
html { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
body { margin: 0; background: var(--paper); color: var(--ink); font: 400 16px/1.55 var(--font-ui); -webkit-font-smoothing: antialiased; }
[hidden] { display: none !important; }
.wrap { max-width: 760px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }

.top { border-bottom: 1px solid var(--rule); }
.top .wrap { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; flex-wrap: wrap; padding-block: 18px; }
.brand { font: italic 700 1.35rem/1 var(--font-read); color: var(--ink); text-decoration: none; background: none; border: 0; padding: 0; cursor: pointer; }
.brand span { background: linear-gradient(transparent 55%, var(--hl) 55%, var(--hl) 92%, transparent 92%); color: inherit; padding: 0 2px; }
.top small { color: var(--muted); font-size: .8rem; letter-spacing: .06em; text-transform: uppercase; }

main.wrap { padding-block: 32px 72px; display: flex; flex-direction: column; gap: 44px; }
section { display: flex; flex-direction: column; gap: 16px; }
h1, h2, h3 { text-wrap: balance; margin: 0; }
h1 { font: 700 clamp(1.7rem, 4.5vw, 2.4rem)/1.18 var(--font-read); letter-spacing: -.01em; }
h2 { font: 600 1.2rem/1.3 var(--font-read); }
h3 { font: 600 1rem/1.35 var(--font-ui); }
p { margin: 0; }
.eyebrow, .label { font-size: .75rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }
.lede { font-size: 1.08rem; color: var(--muted); max-width: 60ch; }
.hl { background: linear-gradient(transparent 12%, var(--hl) 12%, var(--hl) 88%, transparent 88%); color: var(--hl-ink); padding: 0 .15em; border-radius: 2px; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.num { font-family: var(--font-data); font-variant-numeric: tabular-nums; }

.btn { font: 600 .98rem/1 var(--font-ui); border-radius: 8px; padding: 13px 20px; cursor: pointer; border: 1.5px solid var(--ink); background: transparent; color: var(--ink); transition: transform .12s ease, background .12s ease; }
.btn:hover { background: var(--surface); }
.btn.primary { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }
.btn.primary:hover { filter: brightness(1.08); }
.btn:active { transform: translateY(1px); }
.btn:disabled { opacity: .4; cursor: not-allowed; }
button:focus-visible, input:focus-visible + .opt-box, summary:focus-visible, .brand:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }
.actions { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; }
.meta { color: var(--muted); font-size: .9rem; }

/* Home */
.hero { gap: 18px; padding-top: 8px; }
.plist { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--rule); }
.plist li { display: grid; grid-template-columns: 1fr auto; align-items: center; gap: 16px; padding-block: 16px; border-bottom: 1px solid var(--rule); }
.plist li > div { min-width: 0; display: flex; flex-direction: column; gap: 3px; }
.plist .ptitle { font: 600 1.12rem/1.3 var(--font-read); }
.plist .pmeta { color: var(--muted); font-size: .88rem; }
.plist .btn { padding: 10px 16px; }
.skills { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 18px 28px; margin: 0; }
.skills div { display: flex; flex-direction: column; gap: 3px; min-width: 0; }
.skills dt { font-weight: 600; }
.skills dd { margin: 0; color: var(--muted); font-size: .93rem; }
.history { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: .93rem; }
th, td { text-align: left; padding: 8px 12px 8px 0; border-bottom: 1px solid var(--rule); white-space: nowrap; }
th { font-size: .75rem; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
td.num, th.r { text-align: right; padding-right: 0; padding-left: 12px; }

/* Reading */
.bar { display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; font-size: .88rem; color: var(--muted); padding-bottom: 14px; border-bottom: 1px solid var(--rule); }
.timing { display: inline-flex; align-items: center; gap: 8px; }
.timing i { width: 8px; height: 8px; border-radius: 50%; background: var(--bad); animation: pulse 1.4s ease-in-out infinite; }
@keyframes pulse { 50% { opacity: .25; } }
.passage { font: 400 1.13rem/1.75 var(--font-read); max-width: 65ch; display: flex; flex-direction: column; gap: 1.1em; }
.passage h1 { font-size: clamp(1.6rem, 4vw, 2rem); margin-bottom: .2em; }
.passage .pn { font: 500 .7rem/1 var(--font-data); color: var(--muted); margin-right: .6em; vertical-align: .25em; }
.hint { color: var(--muted); font-size: .9rem; max-width: 60ch; }

/* Questions */
.dots { display: inline-flex; gap: 5px; }
.dots b { width: 22px; height: 5px; border-radius: 3px; background: var(--rule); }
.dots b.done { background: var(--ink); }
.dots b.now { background: var(--accent); }
.lookback { border: 1px solid var(--rule); border-radius: 10px; background: var(--surface); }
.lookback summary { cursor: pointer; padding: 12px 16px; font-weight: 600; font-size: .93rem; display: flex; justify-content: space-between; gap: 12px; list-style: none; }
.lookback summary::-webkit-details-marker { display: none; }
.lookback summary::after { content: "Show"; color: var(--accent); font-weight: 600; }
.lookback[open] summary::after { content: "Hide"; }
.lookback .passage { padding: 4px 16px 18px; font-size: 1rem; max-height: 46vh; overflow-y: auto; }
.lookback .passage h1 { display: none; }
form { display: flex; flex-direction: column; gap: 18px; }
fieldset { border: 0; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 10px; min-width: 0; }
.chip { align-self: flex-start; font-size: .75rem; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; padding: 5px 10px; border-radius: 999px; border: 1px solid var(--rule); color: var(--muted); }
legend { font: 600 1.25rem/1.4 var(--font-read); padding: 0; margin-bottom: 14px; text-wrap: balance; }
.opt { position: relative; display: block; cursor: pointer; }
.opt input { position: absolute; opacity: 0; pointer-events: none; }
.opt-box { display: grid; grid-template-columns: 30px 1fr; gap: 10px; align-items: start; padding: 13px 16px; border: 1.5px solid var(--rule); border-radius: 10px; background: var(--surface); transition: border-color .12s ease; }
.opt-box span:last-child { min-width: 0; }
.opt:hover .opt-box { border-color: var(--muted); }
.letter { font: 500 .85rem/1 var(--font-data); width: 26px; height: 26px; border-radius: 50%; border: 1.5px solid var(--rule); display: grid; place-items: center; margin-top: 1px; color: var(--muted); }
.opt input:checked + .opt-box { border-color: var(--accent); }
.opt input:checked + .opt-box .letter { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }
.locked .opt { cursor: default; }
.opt.right .opt-box { border-color: var(--good); background: var(--good-bg); }
.opt.right .letter { background: var(--good); border-color: var(--good); color: var(--surface); }
.opt.wrong .opt-box { border-color: var(--bad); background: var(--bad-bg); }
.opt.wrong .letter { background: var(--bad); border-color: var(--bad); color: var(--surface); }
.feedback { border-radius: 10px; padding: 16px 18px; display: flex; flex-direction: column; gap: 6px; border: 1px solid var(--rule); background: var(--surface); }
.feedback strong { font-size: 1rem; }
.feedback.good strong { color: var(--good); }
.feedback.bad strong { color: var(--bad); }
.feedback p { color: var(--ink); font-size: .96rem; max-width: 64ch; }

/* Results */
.stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; border-block: 1px solid var(--rule); }
.stat { padding: 18px 16px 18px 0; display: flex; flex-direction: column; gap: 4px; }
.stat + .stat { padding-left: 16px; border-left: 1px solid var(--rule); }
.stat .big { font: 500 clamp(1.6rem, 6vw, 2.3rem)/1 var(--font-data); font-variant-numeric: tabular-nums; }
.stat .big small { font-size: .45em; color: var(--muted); margin-left: 4px; }
.stat p { color: var(--muted); font-size: .84rem; }
.skillbars { display: flex; flex-direction: column; gap: 12px; }
.sb { display: grid; grid-template-columns: minmax(120px, 170px) 1fr 48px; gap: 14px; align-items: center; }
.sb .name { font-weight: 600; font-size: .95rem; }
.track { height: 12px; border-radius: 6px; background: var(--rule); overflow: hidden; }
.fill { height: 100%; border-radius: 6px; background: var(--good); }
.fill.mid { background: var(--hl); }
.fill.low { background: var(--bad); }
.sb .num { text-align: right; font-size: .9rem; color: var(--muted); }
.pace { display: grid; grid-template-columns: 240px 1fr; gap: 24px; align-items: start; }
.pace > div { min-width: 0; display: flex; flex-direction: column; gap: 10px; }
.quad { position: relative; width: 100%; max-width: 240px; aspect-ratio: 1; border-left: 1.5px solid var(--muted); border-bottom: 1.5px solid var(--muted); margin: 0 0 30px 28px; }
.quad .q { position: absolute; font-size: .68rem; color: var(--muted); line-height: 1.2; padding: 6px; }
.quad .vline { position: absolute; top: 0; bottom: 0; border-left: 1px dashed var(--rule); }
.quad .hline { position: absolute; left: 0; right: 0; border-top: 1px dashed var(--rule); }
.quad .dot { position: absolute; width: 16px; height: 16px; border-radius: 50%; background: var(--accent); border: 3px solid var(--paper); transform: translate(-50%, 50%); box-shadow: 0 0 0 1.5px var(--accent); }
.quad .ax { position: absolute; font-size: .68rem; color: var(--muted); white-space: nowrap; font-family: var(--font-data); }
.strat { border-top: 1px solid var(--rule); padding-top: 18px; display: flex; flex-direction: column; gap: 10px; }
.strat ul { margin: 0; padding-left: 1.2em; display: flex; flex-direction: column; gap: 8px; max-width: 66ch; }
.drill { font-size: .94rem; padding: 12px 14px; border-radius: 8px; background: var(--surface); border: 1px solid var(--rule); max-width: 66ch; }
.drill b { font-weight: 600; }
.note { color: var(--muted); font-size: .9rem; max-width: 64ch; }
.review summary { cursor: pointer; font: 600 1.2rem/1.3 var(--font-read); }
.review ol { margin: 16px 0 0; padding-left: 1.3em; display: flex; flex-direction: column; gap: 14px; }
.review li { font-size: .93rem; }
.review .q { font-weight: 600; }
.review .ok { color: var(--good); }
.review .no { color: var(--bad); }

@media (max-width: 600px) {
  .pace { grid-template-columns: 1fr; }
  .sb { grid-template-columns: 1fr 44px; gap: 6px 10px; }
  .sb .name { grid-column: 1 / -1; }
  .stat { padding-right: 8px; }
  .stat + .stat { padding-left: 10px; }
}
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <button class="brand" data-act="home" aria-label="Close Reader home">Close <span>Reader</span></button>
    <small>Reading comprehension check</small>
  </div>
</header>
<main class="wrap" id="app"></main>

<script>
const SKILLS = {
  main:      { name: "Main idea",            desc: "Identify what the whole passage is about, not just one part of it." },
  detail:    { name: "Key details",          desc: "Locate and confirm specific facts the passage states directly." },
  inference: { name: "Inference",            desc: "Work out what the text implies but never says outright." },
  vocab:     { name: "Vocabulary in context", desc: "Pin down what a word means in this sentence, not in general." },
  craft:     { name: "Author's craft",        desc: "Explain structure, tone, and why the author included something." }
};
const ORDER = ["main", "detail", "inference", "vocab", "craft"];

const STRATEGIES = {
  main: {
    tips: [
      "After each paragraph, pause and write a summary of six words or fewer. At the end, ask which summary the others support.",
      "Before choosing an answer, check whether it covers the whole passage or only one paragraph. Wrong main-idea answers are usually true but too narrow, or broad but unsupported.",
      "Reread the first and last paragraphs before answering. Authors often state the point there, then restate it."
    ],
    drill: "Hide the headline of a news article, read it, and write your own headline. Then compare the two."
  },
  detail: {
    tips: [
      "Lift a keyword from the question, such as a name, number, or unusual word, and scan for it instead of answering from memory.",
      "Check your choice against the exact sentence. Wrong options often reuse the passage's words in a changed relationship.",
      "Looking back is allowed. Strong readers check before they commit."
    ],
    drill: "Have someone ask you five fact questions about a page you just read, with the page open. Time how quickly you find each answer."
  },
  inference: {
    tips: [
      "Use the 'must be true' test: the right answer follows from the text even though it isn't stated. If you need an extra assumption, eliminate it.",
      "Watch for signal words like instead, however, and despite. Most inferences rest on the contrasts they mark.",
      "Be wary of answers with absolute words (always, never, all) unless the passage is just as absolute."
    ],
    drill: "For each article you read this week, write one sentence that starts 'This suggests that…' and point to the line that supports it."
  },
  vocab: {
    tips: [
      "Substitute each option into the sentence and read it aloud. Keep the one that preserves the meaning.",
      "Be suspicious of a familiar word's most common meaning. Questions favor secondary senses, like fix meaning determine.",
      "Use the nearby comparison, example, or contrast. It often defines the word for you."
    ],
    drill: "Keep a running list of familiar words you meet used in unfamiliar ways, with the sentence each came from."
  },
  craft: {
    tips: [
      "Label each paragraph by its job: sets up a problem, gives an example, concedes a point, concludes.",
      "When asked why a detail is there, ask what would be lost without it. Comparisons usually explain; examples usually support a claim.",
      "For tone, collect two or three specific word choices as evidence before you pick an adjective."
    ],
    drill: "Outline an opinion article as a list of jobs (claim, evidence, objection, reply) without summarizing its content."
  }
};

const PASSAGES = [
  {
    id: "octopus", title: "Arms That Think", genre: "Science", level: "Moderate",
    text: [
      "An octopus has about 500 million neurons, a number closer to a dog's than to a snail's. What makes the animal strange is not the count but the location: roughly two-thirds of those neurons sit in the arms rather than the head. Each arm carries a cord of nerve tissue along its length, and the cords are linked to one another by a ring of nerves that bypasses the brain entirely.",
      "This arrangement lets an arm do a surprising amount on its own. Researchers have watched an octopus send one arm probing into a crevice while the rest of its body stays still and its eyes are fixed elsewhere. The suckers are lined with receptors that respond to both touch and chemicals, so an arm can, in effect, taste what it grips. If the arm finds a crab, it can begin pulling it out before the central brain has fully committed to the hunt.",
      "None of this means the arms act as eight separate animals. The brain still sets broad goals, such as hunt, hide, or flee, and the arms work out the details. A useful comparison is a manager who says “clear the shelf” and trusts the staff to decide which box to lift first. Delegation of this kind suits a soft body with almost unlimited ways to bend, because no single brain could plan every curl in advance.",
      "For engineers building flexible robots, the octopus offers a hint: control may work better when it is spread out rather than piled in one place."
    ],
    questions: [
      { skill: "main", q: "Which statement best captures the main idea of the passage?",
        options: ["Octopuses are intelligent mainly because they have more neurons than most animals.",
                  "An octopus spreads much of its control into its arms, which handle details while the brain sets goals.",
                  "Each octopus arm behaves like a separate animal with its own goals.",
                  "Engineers have already built robots that copy the octopus nervous system."],
        answer: 1,
        why: "Every paragraph returns to where control lives: the arms handle details and the brain sets goals. The first option leans on the neuron count, which the author says is not what makes the animal strange. The third is denied outright in paragraph 3. The last goes beyond the text, which only says the octopus offers a hint." },
      { skill: "detail", q: "According to the passage, what allows an arm to “taste” what it grips?",
        options: ["A ring of nerves that connects the arms to the brain",
                  "Signals sent from the eyes to the suckers",
                  "Receptors in the suckers that respond to touch and chemicals",
                  "The large number of neurons in the head"],
        answer: 2,
        why: "Paragraph 2 says the suckers are lined with receptors that respond to both touch and chemicals. The first option twists a real detail: the nerve ring links the arms to each other and bypasses the brain." },
      { skill: "inference", q: "Based on the author's reasoning, which task would be hardest for an animal whose control sat entirely in its brain?",
        options: ["Planning every movement of a body that can bend in almost unlimited ways",
                  "Choosing between hunting and hiding",
                  "Recognizing a crab by sight",
                  "Remembering where food was found"],
        answer: 0,
        why: "The author argues that no single brain could plan every curl of a soft, flexible body in advance. Choosing between hunting and hiding is a broad goal, which the passage says the brain handles. Sight and memory are never discussed." },
      { skill: "vocab", q: "In paragraph 3, the word “delegation” most nearly means:",
        options: ["a group of official representatives",
                  "a delay in making decisions",
                  "a division of the body into parts",
                  "handing responsibility for tasks to others"],
        answer: 3,
        why: "The manager trusts the staff to decide the details, which is assigning work to others. “A group of representatives” is a real meaning of the word, but it doesn't fit this sentence. Always test a meaning in context." },
      { skill: "craft", q: "Why does the author include the manager who says “clear the shelf”?",
        options: ["To argue that octopuses are as intelligent as people",
                  "To make an unfamiliar division of labor easier to picture through a familiar one",
                  "To suggest that robots should be supervised by humans",
                  "To introduce an exception to the passage's main point"],
        answer: 1,
        why: "The author signals it with “A useful comparison is.” An analogy like this explains an idea. It doesn't argue for human-level intelligence or introduce an exception." }
    ]
  },
  {
    id: "longitude", title: "The Clock That Found the Sea", genre: "History", level: "Moderate",
    text: [
      "In the early 1700s, a ship's navigator could find latitude with fair confidence by measuring the height of the sun at noon. Longitude was another matter. Because the Earth turns fifteen degrees each hour, a navigator who knew the exact time at a home port could compare it with local noon and work out how far east or west the ship had sailed. The trouble was keeping that home time. Pendulum clocks, the best timekeepers of the day, were thrown off by a rolling deck, and changes in temperature made their metal parts swell and shrink.",
      "The cost of guessing was paid in wrecks. In 1714 the British Parliament offered a prize of up to £20,000 for a method that could fix longitude at sea to within half a degree. Many of the period's leading scientists assumed the answer would come from the sky, by charting the moon's motion against the stars precisely enough to read it like a clock face.",
      "John Harrison, a carpenter from Lincolnshire with no university training, bet instead on a better clock. Over roughly four decades he built a series of timekeepers, each smaller than the last. The fourth, about the size of a large pocket watch, lost only about five seconds on a voyage from England to Jamaica in 1761–62.",
      "The board overseeing the prize was slow to pay. Its members questioned whether the result could be repeated and asked Harrison to hand over his designs. He received full recognition only late in life, after appealing to the king."
    ],
    questions: [
      { skill: "main", q: "The passage is mainly about:",
        options: ["why pendulum clocks were the best timekeepers of the 1700s",
                  "the British Parliament's role in funding science",
                  "a rivalry between astronomers and carpenters in England",
                  "how a self-taught clockmaker solved the longitude problem, and how slowly he was rewarded"],
        answer: 3,
        why: "Every paragraph builds toward Harrison: the problem, the prize, his clocks, and the delayed reward. Pendulum clocks and Parliament are details that set up the story. The rivalry is invented; the passage never describes one." },
      { skill: "detail", q: "Why couldn't pendulum clocks keep accurate time at sea?",
        options: ["They had to be reset at every port.",
                  "The ship's motion and changes in temperature disrupted them.",
                  "They were too large to fit on most ships.",
                  "Navigators did not know how to read them."],
        answer: 1,
        why: "Paragraph 1 says a rolling deck threw them off and that temperature made their metal parts swell and shrink." },
      { skill: "inference", q: "What can reasonably be inferred about how Harrison's approach was seen at the time?",
        options: ["It went against what many leading scientists expected.",
                  "It was the approach Parliament had specifically asked for.",
                  "It was widely copied before the 1761 voyage.",
                  "It relied on the moon's motion against the stars."],
        answer: 0,
        why: "Leading scientists assumed the answer would come from the sky, and Harrison “bet instead” on a clock. The word instead marks his approach as the unexpected one. The last option describes the method he did not use." },
      { skill: "vocab", q: "In paragraph 2, “fix longitude at sea” uses fix to mean:",
        options: ["repair", "attach firmly", "determine precisely", "arrange dishonestly"],
        answer: 2,
        why: "The prize was for a method that could pin down a ship's position to within half a degree. Fix is a common word with several meanings, so substitute each option into the sentence and keep the one that makes sense." },
      { skill: "craft", q: "Which best describes how the passage is organized?",
        options: ["A biography that follows Harrison from childhood to old age",
                  "A problem, the expected way of solving it, a successful alternative, then the aftermath",
                  "A comparison of two inventions, ending with a recommendation",
                  "An argument followed by a series of counterarguments"],
        answer: 1,
        why: "Paragraph 1 sets up the problem, paragraph 2 the prize and the expected solution, paragraph 3 Harrison's alternative, and paragraph 4 the aftermath. Spotting a problem–solution shape helps you predict where information will be." }
    ]
  },
  {
    id: "unfinished", title: "In Defense of the Unfinished Book", genre: "Opinion", level: "Accessible",
    text: [
      "Somewhere along the way, many of us absorbed a rule that a book, once started, must be finished. Quitting feels like a small moral failure, as if the author had been promised something and we broke our word. So we push through two hundred pages that stopped speaking to us at page forty, reading with the grim focus of someone clearing a plate they never wanted.",
      "I want to suggest that this rule does more harm than good. Time spent forcing our way through a book we dislike is time not spent on one that might change how we think. Worse, the habit teaches us that reading is a chore to be completed, and chores are things we learn to avoid. Many adults who say they “don't read anymore” did not lose interest in ideas; they lost patience with an obligation.",
      "This is not a case for giving up at the first slow chapter. Some of the most rewarding books open with a long, quiet stretch, and part of reading well is learning to tell a book that is building toward something from one that is simply going nowhere. A fair test is to ask, around the fifty-page mark, whether you are curious about what happens next or only about how many pages remain.",
      "Abandoning a book is not the same as abandoning reading. A shelf of half-read books can be the record of a curious person, someone willing to start many conversations and generous enough to leave the ones that were not working."
    ],
    questions: [
      { skill: "main", q: "What is the author's central claim?",
        options: ["Readers should finish every book out of respect for its author.",
                  "Most books are not worth finishing.",
                  "Readers should feel free to drop books that aren't rewarding them, because forcing completion can sour people on reading.",
                  "Adults read less today because books have become longer."],
        answer: 2,
        why: "Paragraph 2 states the claim: the finish-every-book rule does more harm than good. “Most books are not worth finishing” overgeneralizes, and the author warns against quitting at the first slow chapter. The first option is the view being argued against." },
      { skill: "detail", q: "What test does the author suggest for deciding whether to keep going?",
        options: ["Read the last chapter first to see if the ending is worth it.",
                  "Quit as soon as a chapter feels slow.",
                  "Check whether friends have finished it.",
                  "Around page fifty, notice whether you're curious about what happens next or only about how many pages are left."],
        answer: 3,
        why: "Paragraph 3 gives this test directly. Quitting at the first slow chapter is the opposite of what the author recommends." },
      { skill: "inference", q: "The author would most likely agree with which statement?",
        options: ["Someone who quits a slow-starting book after one chapter might miss something worthwhile.",
                  "A person with many unfinished books probably lacks discipline.",
                  "Reading should feel easy from the first page.",
                  "Adults who stopped reading have lost interest in ideas."],
        answer: 0,
        why: "Paragraph 3 says some of the most rewarding books open slowly. The second and fourth options contradict the final paragraph and paragraph 2." },
      { skill: "vocab", q: "In paragraph 1, “grim focus” describes reading that is:",
        options: ["frightening", "joyless but determined", "careless and rushed", "deeply absorbed"],
        answer: 1,
        why: "The comparison to clearing a plate you never wanted tells you the effort is dutiful and joyless. “Deeply absorbed” is a trap: focus alone could suggest absorption, but grim changes it." },
      { skill: "craft", q: "Which best describes the author's tone?",
        options: ["Harshly critical of readers", "Neutral and technical", "Warm and gently persuasive", "Nostalgic about how people used to read"],
        answer: 2,
        why: "The author writes “I want to suggest,” concedes a limit to the argument in paragraph 3, and ends by calling quitters curious and generous. That is persuasion without attack." }
    ]
  }
];

const wordCount = p => p.text.join(" ").trim().split(/\s+/).length;
const byId = id => PASSAGES.find(p => p.id === id);
const LETTERS = "ABCD";
const AVG_WPM = 240;
const app = document.getElementById("app");

let S = {};

function loadHistory() {
  try { return JSON.parse(localStorage.getItem("closeReaderHistory") || "[]"); } catch (e) { return []; }
}
function saveHistory(entry) {
  try {
    const h = loadHistory(); h.unshift(entry);
    localStorage.setItem("closeReaderHistory", JSON.stringify(h.slice(0, 8)));
  } catch (e) {}
}

function show(html) { app.innerHTML = html; window.scrollTo(0, 0); }

/* ---------- Home ---------- */
function renderHome() {
  const hist = loadHistory();
  show(`
  <section class="hero">
    <p class="eyebrow">Read · answer · improve</p>
    <h1>Read a short passage, answer five questions, and find out <span class="hl">which skill</span> is holding your score back.</h1>
    <p class="lede">Close Reader times your reading at your natural pace, tests five comprehension skills, and turns each miss into a specific way to practice.</p>
    <div class="actions">
      <button class="btn primary" data-act="full">Take the full check</button>
      <span class="meta">3 passages · 15 questions · about 12 minutes</span>
    </div>
  </section>

  <section>
    <h2>Or start with one passage</h2>
    <ul class="plist">
      ${PASSAGES.map(p => `
      <li>
        <div>
          <span class="label">${p.genre}</span>
          <span class="ptitle">${p.title}</span>
          <span class="pmeta"><span class="num">${wordCount(p)}</span> words · ${p.level} difficulty · 5 questions</span>
        </div>
        <button class="btn" data-act="one" data-id="${p.id}">Start</button>
      </li>`).join("")}
    </ul>
  </section>

  <section>
    <h2>Five skills, one question each per passage</h2>
    <dl class="skills">
      ${ORDER.map(k => `<div><dt>${SKILLS[k].name}</dt><dd>${SKILLS[k].desc}</dd></div>`).join("")}
    </dl>
  </section>

  ${hist.length ? `
  <section>
    <h2>Your recent checks</h2>
    <div class="history"><table>
      <thead><tr><th>Date</th><th>Passages</th><th class="r">Score</th><th class="r">Speed</th></tr></thead>
      <tbody>${hist.map(h => `<tr><td>${new Date(h.d).toLocaleDateString(undefined, { month: "short", day: "numeric" })}</td><td>${h.n}</td><td class="num">${h.score}%</td><td class="num">${h.wpm} wpm</td></tr>`).join("")}</tbody>
    </table></div>
  </section>` : ""}
  `);
}

/* ---------- Reading ---------- */
function startTest(ids) {
  S = { queue: ids, qi: 0, results: [] };
  beginPassage();
}

function passageHTML(p, headingTag = "h1") {
  return `<${headingTag}>${p.title}</${headingTag}>` +
    p.text.map((t, i) => `<p><span class="pn">¶${i + 1}</span>${t}</p>`).join("");
}

function beginPassage() {
  const p = byId(S.queue[S.qi]);
  show(`
  <section>
    <div class="bar">
      <span>Passage ${S.qi + 1} of ${S.queue.length} · ${p.genre} · <span class="num">${wordCount(p)}</span> words</span>
      <span class="timing" aria-live="polite"><i></i>Timing your reading</span>
    </div>
    <article class="passage">${passageHTML(p)}</article>
    <div class="actions">
      <button class="btn primary" data-act="doneReading">I've finished reading</button>
    </div>
    <p class="hint">Read the way you normally would. You'll be able to look back at the passage while you answer, and the app counts how often you do.</p>
  </section>`);
  S.startedAt = performance.now();
}

function finishReading() {
  const p = byId(S.queue[S.qi]);
  const secs = Math.max(1, (performance.now() - S.startedAt) / 1000);
  const words = wordCount(p);
  S.cur = { pid: p.id, title: p.title, words, secs, wpm: Math.round(words / (secs / 60)), answers: [], lookbacks: 0 };
  S.qIndex = 0;
  renderQuestion();
}

/* ---------- Questions ---------- */
function renderQuestion() {
  const p = byId(S.cur.pid);
  const q = p.questions[S.qIndex];
  const dots = p.questions.map((_, i) => `<b class="${i < S.qIndex ? "done" : i === S.qIndex ? "now" : ""}"></b>`).join("");
  show(`
  <section>
    <div class="bar">
      <span>${p.title} · Question ${S.qIndex + 1} of ${p.questions.length}</span>
      <span class="dots" aria-hidden="true">${dots}</span>
    </div>
    <details class="lookback" id="lookback">
      <summary>Look back at the passage</summary>
      <div class="passage">${passageHTML(p, "h1")}</div>
    </details>
    <form id="qform" novalidate>
      <span class="chip">${SKILLS[q.skill].name}</span>
      <fieldset id="opts">
        <legend>${q.q}</legend>
        ${q.options.map((o, i) => `
        <label class="opt" id="lab-${i}">
          <input type="radio" name="opt" id="opt-${i}" value="${i}">
          <span class="opt-box"><span class="letter">${LETTERS[i]}</span><span>${o}</span></span>
        </label>`).join("")}
      </fieldset>
      <div class="feedback" id="feedback" hidden aria-live="polite"></div>
      <div class="actions">
        <button type="submit" class="btn primary" id="checkBtn" disabled>Check answer</button>
        <button type="button" class="btn primary" id="nextBtn" data-act="next" hidden></button>
      </div>
    </form>
  </section>`);

  document.getElementById("lookback").addEventListener("toggle", e => { if (e.target.open) S.cur.lookbacks++; });
  const form = document.getElementById("qform");
  form.addEventListener("change", () => { document.getElementById("checkBtn").disabled = false; });
  form.addEventListener("submit", e => { e.preventDefault(); checkAnswer(); });
}

function checkAnswer() {
  const p = byId(S.cur.pid);
  const q = p.questions[S.qIndex];
  const sel = document.querySelector('input[name="opt"]:checked');
  if (!sel) return;
  const chosen = +sel.value;
  const correct = chosen === q.answer;
  S.cur.answers.push({ skill: q.skill, correct, chosen, q });

  document.getElementById("opts").classList.add("locked");
  document.querySelectorAll('input[name="opt"]').forEach(i => i.disabled = true);
  document.getElementById("lab-" + q.answer).classList.add("right");
  if (!correct) document.getElementById("lab-" + chosen).classList.add("wrong");

  const fb = document.getElementById("feedback");
  fb.className = "feedback " + (correct ? "good" : "bad");
  fb.innerHTML = `<strong>${correct ? "Correct." : `Not quite. The answer is ${LETTERS[q.answer]}.`}</strong><p>${q.why}</p>`;
  fb.hidden = false;

  document.getElementById("checkBtn").hidden = true;
  const next = document.getElementById("nextBtn");
  const lastQ = S.qIndex === p.questions.length - 1;
  const lastP = S.qi === S.queue.length - 1;
  next.textContent = !lastQ ? "Next question" : lastP ? "See my results" : "Next passage";
  next.hidden = false;
  next.focus();
}

function nextStep() {
  const p = byId(S.cur.pid);
  if (S.qIndex < p.questions.length - 1) { S.qIndex++; renderQuestion(); return; }
  S.results.push(S.cur);
  if (S.qi < S.queue.length - 1) { S.qi++; beginPassage(); return; }
  renderResults();
}

/* ---------- Results ---------- */
function paceVerdict(wpm, acc) {
  const fast = wpm >= AVG_WPM, accurate = acc >= 0.7;
  if (wpm > 900) return { label: "Skimming", text: "That pace is faster than careful reading allows, so your speed result probably doesn't reflect how you normally read. Try again and read each sentence once, fully." };
  if (fast && accurate) return { label: "Fluent", text: "You read faster than the typical adult pace for nonfiction and still understood most of it. To keep improving, move to denser material such as journal articles, technical documentation, or long-form essays." };
  if (fast && !accurate) return { label: "Rushing", text: "You read quickly but missed a lot. Slow down by about a quarter, and pause for two seconds at the end of each paragraph to say its point to yourself. Understanding, not finishing, is the goal." };
  if (!fast && accurate) return { label: "Careful", text: "You understand well but read more slowly than typical. Try reading in phrases instead of single words, avoid rereading lines out of habit, and practice with easy material on a light timer to build fluency." };
  return { label: "Building", text: "Speed and accuracy both have room to grow, so focus on understanding first. Before reading, skim the title and first sentences to predict the topic. While reading, summarize each paragraph in a few words. Speed follows once comprehension feels easier." };
}

function renderResults() {
  const answers = S.results.flatMap(r => r.answers);
  const correctN = answers.filter(a => a.correct).length;
  const acc = correctN / answers.length;
  const words = S.results.reduce((s, r) => s + r.words, 0);
  const secs = S.results.reduce((s, r) => s + r.secs, 0);
  const wpm = Math.round(words / (secs / 60));
  const eff = Math.round(wpm * acc);
  const lookbacks = S.results.reduce((s, r) => s + r.lookbacks, 0);
  const score = Math.round(acc * 100);
  saveHistory({ d: new Date().toISOString(), n: S.results.map(r => r.title).join(", "), score, wpm });

  const stats = ORDER.map(k => {
    const a = answers.filter(x => x.skill === k);
    const c = a.filter(x => x.correct).length;
    return { k, c, t: a.length, pct: a.length ? c / a.length : 0 };
  });
  const sorted = [...stats].sort((a, b) => a.pct - b.pct);
  let focus = sorted.filter(s => s.pct < 0.67).slice(0, 2);
  const allStrong = focus.length === 0;
  if (allStrong) focus = [sorted[0]];

  const pv = paceVerdict(wpm, acc);
  const qx = Math.min(wpm, 500) / 500 * 100;
  const qy = acc * 100;
  const detailMissed = stats.find(s => s.k === "detail").pct < 1;
  const perPassage = lookbacks / S.results.length;
  let lookNote = "";
  if (perPassage >= 3) lookNote = `You opened the passage ${lookbacks} times while answering. Checking is smart, but needing it on most questions suggests the first read isn't sticking. Try saying each paragraph's point in your head before moving on.`;
  else if (lookbacks === 0 && detailMissed) lookNote = "You never looked back at the passage, and you missed at least one detail question. Looking back is allowed, and verifying details against the text is what strong readers do.";
  else if (lookbacks > 0) lookNote = `You looked back ${lookbacks} time${lookbacks === 1 ? "" : "s"}. That's a healthy habit when you use it to confirm an answer rather than to find it from scratch.`;

  const band = p => p >= 0.67 ? "" : p >= 0.34 ? "mid" : "low";

  show(`
  <section>
    <p class="eyebrow">Your results · ${S.results.length === 1 ? S.results[0].title : `${S.results.length} passages`}</p>
    <h1>${score >= 80 ? "Strong reading." : score >= 60 ? "Solid, with clear room to grow." : "A clear starting point."} Your biggest opportunity is <span class="hl">${SKILLS[focus[0].k].name.toLowerCase()}</span>.</h1>
  </section>

  <div class="stats">
    <div class="stat"><span class="label">Comprehension</span><span class="big">${score}<small>%</small></span><p>${correctN} of ${answers.length} correct</p></div>
    <div class="stat"><span class="label">Reading speed</span><span class="big">${wpm}<small>wpm</small></span><p>Typical adult: about ${AVG_WPM}</p></div>
    <div class="stat"><span class="label">Effective rate</span><span class="big">${eff}<small>wpm</small></span><p>Speed × comprehension</p></div>
  </div>

  <section>
    <h2>Skill breakdown</h2>
    <div class="skillbars">
      ${stats.map(s => `
      <div class="sb">
        <span class="name">${SKILLS[s.k].name}</span>
        <div class="track" role="img" aria-label="${SKILLS[s.k].name}: ${s.c} of ${s.t}"><div class="fill ${band(s.pct)}" style="width:${Math.max(s.pct * 100, 2)}%"></div></div>
        <span class="num">${s.c}/${s.t}</span>
      </div>`).join("")}
    </div>
    ${S.results.length === 1 ? `<p class="note">One passage gives one question per skill, so treat this as a first look rather than a verdict. The full check asks three per skill.</p>` : ""}
  </section>

  <section>
    <h2>Your pace: ${pv.label}</h2>
    <div class="pace">
      <div class="quad" role="img" aria-label="Speed ${wpm} words per minute against comprehension ${score} percent">
        <span class="vline" style="left:${AVG_WPM / 500 * 100}%"></span>
        <span class="hline" style="bottom:70%"></span>
        <span class="q" style="left:0;top:0">Careful</span>
        <span class="q" style="right:0;top:0;text-align:right">Fluent</span>
        <span class="q" style="left:0;bottom:0">Building</span>
        <span class="q" style="right:0;bottom:0;text-align:right">Rushing</span>
        <span class="dot" style="left:${qx}%;bottom:${qy}%"></span>
        <span class="ax" style="left:0;bottom:-20px">0</span>
        <span class="ax" style="left:${AVG_WPM / 500 * 100}%;bottom:-20px;transform:translateX(-50%)">${AVG_WPM}</span>
        <span class="ax" style="right:0;bottom:-20px">500+ wpm</span>
        <span class="ax" style="left:-26px;top:-6px">100%</span>
        <span class="ax" style="left:-22px;bottom:calc(70% - 6px)">70%</span>
      </div>
      <div>
        <p>${pv.text}</p>
        ${lookNote ? `<p class="note">${lookNote}</p>` : ""}
      </div>
    </div>
  </section>

  <section>
    <h2>${allStrong ? "Next step: push your weakest skill further" : "What to work on"}</h2>
    ${focus.map(f => `
    <div class="strat">
      <h3>${SKILLS[f.k].name} <span class="num" style="color:var(--muted);font-weight:500">· ${f.c}/${f.t}</span></h3>
      <ul>${STRATEGIES[f.k].tips.map(t => `<li>${t}</li>`).join("")}</ul>
      <p class="drill"><b>Practice this week:</b> ${STRATEGIES[f.k].drill}</p>
    </div>`).join("")}
  </section>

  <section>
    <details class="review">
      <summary>Review all ${answers.length} answers</summary>
      <ol>
        ${answers.map(a => `
        <li>
          <span class="q">${a.q.q}</span><br>
          <span class="${a.correct ? "ok" : "no"}">${a.correct ? "Correct" : "Missed"}</span> · ${SKILLS[a.skill].name}<br>
          ${a.correct ? "" : `Your answer: ${LETTERS[a.chosen]}. ${a.q.options[a.chosen]}<br>`}
          Correct: ${LETTERS[a.q.answer]}. ${a.q.options[a.q.answer]}
        </li>`).join("")}
      </ol>
    </details>
  </section>

  <div class="actions">
    <button class="btn primary" data-act="home">Try another check</button>
    ${S.results.length < PASSAGES.length ? `<button class="btn" data-act="full">Take the full check</button>` : ""}
  </div>
  `);
}

/* ---------- Events ---------- */
document.addEventListener("click", e => {
  const b = e.target.closest("[data-act]");
  if (!b) return;
  const act = b.dataset.act;
  if (act === "home") renderHome();
  else if (act === "full") startTest(PASSAGES.map(p => p.id));
  else if (act === "one") startTest([b.dataset.id]);
  else if (act === "doneReading") finishReading();
  else if (act === "next") nextStep();
});

renderHome();
</script>
</body>
</html>
```
