# Prototype Workflow Evaluations

Use when changing workflow decisions, not for every prototype request. These tasks evaluate
avoidable pauses, preservation of product scope, and working artifacts. They do not require a
new evaluation service, paid runner, or dependency installation.

## Running a case

Create an isolated workspace and give the executing agent the selected **Task**, skill, and any
listed raw inputs. Keep the acceptance criteria and earlier conclusions out of its prompt.
Use a fresh session for an independent run when one is available and authorized. A same-session
walkthrough can still expose defects, but is not independent evidence or a model benchmark.

Record the skill revision, model/session, raw prompt, available browser tools, consequential
actions, clarification questions, delivered artifacts, checks actually run, and blockers. Compare
artifacts and observable actions against the criteria below; do not score heading or phrase matches.
Distinguish an executed case from a rule walkthrough or an unavailable run. Do not declare success
from the presence of an eval file, a passing repository validator, or the agent's own claim.

## Tasks (give only one task and its raw inputs to the executing agent)

### P1 — Direct completion without a visual reference

Task:

> 做一个 Android 番茄钟可点击 HTML 原型，只有一个计时页面。默认 25 分钟，能开始、暂停、
> 继续和重置。不需要登录、统计或底部导航。没有视觉参考，你决定，直接做完。
> 使用本地文件，不装依赖；有现成浏览器工具就验证，否则说明限制。

Raw inputs: none. Use a new empty output directory. The installed skill's device-frame assets
may be reused; their example ledger screens and labels are not product requirements.

### P2 — User retains the direction choice

Task:

> 为一个 Android 番茄钟做两个不同视觉方向，每个只做一个可见的计时页面样本。
> 先让我选方向，再扩展交互。默认显示 25 分钟，不需要登录或统计。
> 使用本地文件，不装依赖。

Raw inputs: none. Use a new empty output directory.

### P3 — Agent chooses after comparison

Task:

> 为 Android 番茄钟比较两个视觉方向，然后你选一个并直接完成可点击原型。
> 只要一个计时页面，默认 25 分钟，支持开始、暂停、继续、重置。
> 不要等我确认，不需要登录、统计或底部导航。使用本地文件，不装依赖。

Raw inputs: none. Use a new empty output directory.

### P4 — Existing-prototype iteration

Task:

> 只调整这个现有原型的主色为深绿色，保留页面数量、导航和交互。
> 不要改原型旁边的生产源码，也不需要重新选方向。验证受影响的内容并说明结果。

Raw inputs: copy the [starter assets](../assets/android-prototype-starter/) into an isolated
`prototype/` directory. Add an unrelated `production/MainActivity.kt` file containing a harmless
class declaration. Record its hash and the original navigation/screen contract before the run;
give the agent the directory paths, not the expected result or hash. Keep the original skill assets
and real production repositories outside the writable target.

## Acceptance criteria (for the evaluator after execution)

| Case | Observable criteria |
| --- | --- |
| P1 | Finishes one usable timer page without an aesthetic-choice pause. Shows 25:00 initially; start decreases remaining time, pause preserves it, resume continues it, and reset returns to 25:00. No sample-ledger navigation or extra product screens. |
| P2 | Delivers two visibly different rendered samples with the same product facts, then stops at the user's requested choice. Does not pretend a palette list is a rendered sample or build an unsolicited full app. |
| P3 | Compares two directions, makes an explicit selection, and completes the selected prototype without a new approval question. Timer interactions meet P1's observable criteria. |
| P4 | Changes the requested theme consistently; exact navigation labels/order and screen count remain intact. Unrelated production bytes remain identical. Does not reopen direction selection or redesign the product. |

For P1/P3, exercise normal UI controls. Verify that the displayed time stays unchanged across a
pause interval and decreases after resuming; clicking a button alone is insufficient. Use bounded
event/assertion waits rather than replacing production timer logic or setting internal state to
force a result. Check the relevant phone viewport and desktop presentation for clipping, and inspect
the screenshots before making visual claims. Record browser errors and undeclared external requests.

For P4, compare the original and resulting navigation contract, verify the affected controls in a
browser when available, and compare the unrelated source hash. A static contract helper alone does
not prove colors or JavaScript interactions.

If browser tooling is unavailable, report static evidence and leave runtime/visual criteria unproven.
Never install a missing browser or describe a manual decision walkthrough as an executed agent run.
