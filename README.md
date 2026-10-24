# Product Site Engineering Skill

一个面向 Codex / ChatGPT Skills 的通用网站工程交付 Skill。它把“帮我做个网站”展开为可审计的工程闭环：需求、产品规范、验收编号、受保护资产、前后端边界、日志与可观测性、测试、部署、回滚和真实用户反馈。

它不是某个框架的脚手架，也不会把 Psyche Guide 的私有提示词、用户内容或业务机密打包出去。仓库中保留的是从真实产品交付中抽象出的通用方法与无敏感数据模板。

## 能做什么

- 从模糊需求建立产品事实来源、非目标和主用户闭环。
- 把“自然、好用、专业、稳定”等主观要求写成有 ID 的验收场景。
- 在 UI 重构前登记受保护的页面、功能入口与已有数据，防止“优化”变成误删。
- 约束前端的空、载入、成功、失败、超时、重试、取消和重复提交状态。
- 约束后端的输入校验、鉴权、限流、幂等、统一错误、请求 ID、迁移与数据隔离。
- 设计不记录正文和秘密的前端事件、后端结构化日志、流式请求生命周期、看板和运行手册。
- 为 AI 网站建立服务端提示、知识治理、记忆同意、输出护栏和坏案例评测方法。
- 把框架迁移与功能开发分开，用行为等价清单、预览环境和回滚证据降低风险。
- 初始化一套可直接放进项目的 `docs/product-workbench/` 工作台，并在 CI 中审计其完整性。

## 优势

1. **产品与工程不脱节**：每次实现先绑定验收 ID，完成标准不是“代码写了”，而是用户场景、失败路径和发布证据一起成立。
2. **保护已有价值**：用资产登记和改版前后映射避免导航、页面、历史数据或未来商业化代码被无意删除。
3. **可观测但不过度采集**：默认采用字段白名单和请求关联，不把用户表单、对话、Cookie、令牌或上游原文写进日志。
4. **AI 不是只改提示词**：把提示、状态、检索、确定性护栏、评测和生产复测拆开，能定位问题出在哪一层。
5. **复用优先**：先用项目已有和成熟能力；只有关键约束确实无法满足时才自建核心设施。
6. **证据诚实**：明确区分“已写规范、自动测试通过、预览验证、生产验证、真实用户验证”，避免虚假的完成感。

## 仓库结构

```text
product-site-engineering-skill/
├── product-site-engineering/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   ├── scripts/
│   └── assets/workbench/
├── tests/
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

这遵循 OpenAI Skill 的目录模型：`SKILL.md` 负责触发条件与核心流程，细节放在 references，可重复动作放在 scripts，可复制模板放在 assets。

## 使用

把 `product-site-engineering/` 目录安装到支持 Skills 的环境，或将它放进 Codex 可发现的 skills 目录。然后直接说：

```text
使用 $product-site-engineering，把这个网站需求做成可验收、可观测、可发布的纵向切片。
```

在任意项目初始化工作台：

```bash
python3 product-site-engineering/scripts/init_workbench.py \
  --target /absolute/path/to/project \
  --project "My Product"

python3 product-site-engineering/scripts/audit_workbench.py \
  --target /absolute/path/to/project
```

初始化器默认写入 `docs/product-workbench/`，不会覆盖已有文件；可先加 `--dry-run` 查看计划。

## 验证

本仓库脚本只依赖 Python 标准库：

```bash
python3 product-site-engineering/scripts/validate_skill.py .
python3 -m unittest discover -s tests -v
```

GitHub Actions 会在 push 和 pull request 时运行同样的检查。

## 它不承诺什么

- 不替代产品负责人对定位、收费、数据、版权和高风险安全边界的判断。
- 不保证任意框架、云平台或地区网络天然适用；这些结论必须以当前官方资料和真实部署测试为准。
- 不把日志等同于监控平台，也不自动创建第三方账号或付费服务。
- 不把提示词规范等同于生产护栏，也不把单次模型成功等同于稳定质量。

## 学习资料

已核验的 Skill、提示工程、评测和参考项目网址及适用边界见 [prompt-learning-resources.md](product-site-engineering/references/prompt-learning-resources.md)。

## License

MIT
