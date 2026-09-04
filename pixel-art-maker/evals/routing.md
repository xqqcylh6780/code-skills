# Routing Examples

## Should trigger

- “做一个 32×32 农田瓦片，只给轮廓。”
- “在 Aseprite 里画一个角色并保存分层源文件。”
- “制作四方向走路精灵表。”
- “检查这套像素瓦片能不能无缝拼接。”
- “告诉我怎么画像素草丛，不要生成图片。”

## Should not trigger

- “写角色移动代码。” → game implementation workflow, not pixel art.
- “做普通高清插画。” → general image creation, not this skill.
- “写 FastAPI 服务。” → `build-backends`.
- “搜索 Aseprite 开源替代品。” → `github-repository-search`.
- “只问 Godot 场景脚本逻辑。” → game/code workflow.

## Conflict cases

- “做像素角色并导入游戏。” → this skill owns art assets and import parameters; game runtime logic remains separate.
- “用户只问 Aseprite 快捷键。” → explain the operation only; do not generate an image.
- “已有轮廓，做最终上色。” → edit from the confirmed outline; do not regenerate an unrelated design.
