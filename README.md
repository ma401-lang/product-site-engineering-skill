<div align="center">
  <img src="product-site-engineering/assets/icon-large.svg" alt="Product Site Engineering Skill" width="168" />
  <h1>Product Site Engineering Skill</h1>
  <p><strong>先冻结 benchmark，再把网站需求交付成可验收、可观测、可发布的真实产品。</strong></p>
  <p>Benchmark-first website delivery for Codex and other Agent Skills-compatible tools.</p>
  <p>
    <a href="https://github.com/ma401-lang/product-site-engineering-skill/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/ma401-lang/product-site-engineering-skill/validate.yml?branch=main&style=flat-square&label=validation" alt="Validation status" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-315B52?style=flat-square" alt="MIT License" /></a>
    <a href="https://github.com/ma401-lang/product-site-engineering-skill/releases/tag/v1.1.0"><img src="https://img.shields.io/badge/version-v1.1.0-CB7A54?style=flat-square" alt="Version 1.1.0" /></a>
  </p>
</div>

> 这不是“生成一个好看的页面”的万能提示词。它是一套网站产品工程工作流：先明确用户结果并冻结质量 benchmark，再连接产品规范、验收编号、前后端边界、日志、测试、部署、回滚和真实反馈。

仓库只保留从真实交付中抽象出的通用方法、脚本和无敏感数据模板，不包含 Psyche Guide 的私有提示词、用户内容或业务机密。

## 为什么做这个 Skill

网站项目最容易在三处跑偏：开工时没有统一的好坏标准；实现中只完成顺利路径或视觉外壳；上线时把“本地能跑”误写成“产品已验证”。结果往往是需求、设计、代码、日志和部署各自正确，却没有形成一个可用的用户闭环。

这个 Skill 把方向和证据放在同一条链上：

```text
用户意图
  -> benchmark v1（当前基线、参考来源、反例、权重、目标）
  -> 产品事实来源与验收 ID
  -> 可运行的纵向切片
  -> 自动测试、预览、生产证据
  -> 脱敏反馈
  -> benchmark v2（先改方向，再改实现）
```

benchmark 不是审美拼贴。它要求记录参考来源及作者、为什么可比、学什么、不复制什么，并把方向转成可观察的评价维度。只要方向发生改变，就先升级 benchmark 和受影响的验收项，再动代码；旧证据不被重写。本仓库也用自己的 [BENCHMARK.md](BENCHMARK.md) 约束 v1.1，而不是只要求别人遵守。

## 能做什么

| 模块 | 交付能力 |
|---|---|
| Benchmark-first | 捕获改动前基线，选择可比参考与标准，登记作者/发布方、反例、权重、目标、验收映射和变更历史 |
| 产品契约 | 从模糊需求建立目标用户、主闭环、非目标、当前事实和稳定验收 ID |
| 资产保护 | 在 UI 重构前登记路由、入口、能力和已保存数据，防止“简化”变成误删或隐藏 |
| 前端质量 | 覆盖空、载入、成功、失败、超时、重试、取消、离线、存储失败和重复提交状态 |
| 后端与数据 | 约束输入校验、鉴权、限流、幂等、统一错误、请求 ID、迁移和租户/用户隔离 |
| 日志与可观测性 | 提供前端事件与后端日志白名单、请求关联、流式生命周期、看板信号和运行手册 |
| AI 产品安全 | 建立服务端提示、知识治理、记忆同意、确定性护栏、坏案例评测和生产复测边界 |
| 发布与迁移 | 用行为等价清单、预览环境、区域实测、发布标识和回滚证据降低框架或托管迁移风险 |
| 用户反馈 | 把脱敏真实失败转成新的验收/评测用例，修改最小责任层并验证回归 |

## 优势在哪

1. **先固定“尺子”**：非琐碎任务必须先冻结 benchmark，发布审计会阻止草稿 benchmark 进入发布结论。
2. **产品与工程不脱节**：实现必须绑定验收 ID；完成标准同时包含用户场景、失败路径和证据层级。
3. **保护已有价值**：资产登记和改版前后映射阻止页面、入口、历史数据或未来商业化代码被无意删除。
4. **可观测但不过度采集**：字段白名单默认排除正文、Cookie、令牌、原始邮箱、完整 IP 和上游私密内容。
5. **AI 不只靠堆提示词**：提示、状态、检索、工具、护栏和评测分层，问题能落到真正负责的层。
6. **复用优先**：先用已有项目能力、官方平台和成熟生态；只有关键约束无法满足时才自建核心设施。
7. **证据诚实**：严格区分已规范、已实现、本地通过、预览通过、生产通过和真实用户验证。

## 教程与执行结构

这个仓库采用“Guide + Skill + Workbench + Checks”四层结构：

```text
product-site-engineering-skill/
├── README.md                              # 项目定位、能力与快速开始
├── BENCHMARK.md                           # 本仓库自身的方向基线与 v1.1 冻结记录
├── product-site-engineering/
│   ├── SKILL.md                           # 精简路由与强制交付流程
│   ├── references/                        # benchmark、前端、后端、日志、AI、发布与学习指南
│   ├── assets/workbench/                  # 可复制的产品工程工作台
│   ├── assets/examples/typescript/        # 可运行的日志示例
│   ├── scripts/                           # 初始化、普通审计、发布审计、Skill 校验
│   └── agents/openai.yaml                 # Skill 展示与默认调用元数据
├── tests/                                 # 工作台与发布门禁回归测试
└── .github/workflows/validate.yml         # 持续集成
```

- `SKILL.md` 只保留触发条件、主流程和安全边界。
- `references/` 在相关任务发生时按需读取，避免把所有教程塞进上下文。
- `scripts/` 承担可重复、确定性的机械检查。
- `assets/` 提供可以复制后再定制的工作台与 schema。

这种拆分遵循 [OpenAI Skills 指南](https://developers.openai.com/api/docs/guides/tools-skills)的渐进披露原则。

## 快速开始

把仓库中的 `product-site-engineering/` 安装到支持 Agent Skills 的环境，然后直接说：

```text
使用 $product-site-engineering，先为这个网站建立并冻结 benchmark，
再把需求做成可验收、可观测、可发布的纵向切片。
```

在一个项目中初始化工作台：

```bash
python3 product-site-engineering/scripts/init_workbench.py \
  --target /absolute/path/to/project \
  --project "My Product"
```

普通审计允许 benchmark 处于草稿，便于学习和规划：

```bash
python3 product-site-engineering/scripts/audit_workbench.py \
  --target /absolute/path/to/project
```

准备发布时使用严格门禁；benchmark 必须已冻结，包含改动前基线、负责人、完整评分尺，以及至少两个带作者/发布方的 HTTPS 参考来源：

```bash
python3 product-site-engineering/scripts/audit_workbench.py \
  --target /absolute/path/to/project \
  --release
```

初始化器默认写入 `docs/product-workbench/`，不会覆盖已有文件；面对陌生目录可先加 `--dry-run` 查看写入计划。

## Benchmark 工作法

新生成的 `BENCHMARK.md` 包含：

- 当前产品基线和改动前证据；
- 两到五个可比产品、标准或本地基线，以及作者/发布方和直接来源；
- 每个参考“学什么”和“不复制什么”；
- 明确的 anti-benchmark；
- 带权重、当前值、目标值、测量方法和验收 ID 的质量维度；
- benchmark 版本、状态、负责人和方向变更历史。

详细规则见 [benchmark-first.md](product-site-engineering/references/benchmark-first.md)，可选学习来源见 [website-building-resources.md](product-site-engineering/references/website-building-resources.md)。

## 验证

仓库脚本只依赖 Python 标准库：

```bash
python3 product-site-engineering/scripts/validate_skill.py .
python3 -m unittest discover -s tests -v
```

GitHub Actions 会在 push 和 pull request 时运行同样的检查。发布包还会校验 Skill 元数据、必需资源、脚本语法、文件数量与大小限制，以及日志 schema 的字段白名单。

## 学习来源

首页的信息节奏参考了 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) 的“为什么存在 → 教程结构 → 能力清单 → 快速开始”，但没有复制内容，也没有加入新闻或社区运营板块。

已核验并标注作者/发布方的网站 Skill、设计、工程流程、Playwright、WCAG、OWASP、性能、SEO、MDN、TanStack Start 与 Cloudflare Workers 资料见 [website-building-resources.md](product-site-engineering/references/website-building-resources.md)。提示工程和评测资料见 [prompt-learning-resources.md](product-site-engineering/references/prompt-learning-resources.md)。

## 它不承诺什么

- 不替代产品负责人对定位、收费、数据、版权和高风险安全边界的判断。
- 不把别人的视觉风格、品牌、提示词或产品结构当成可直接复制的模板。
- 不保证任意框架、云平台或地区网络天然适用；必须使用当前官方资料和真实部署测试。
- 不把日志等同于完整监控平台，也不自动创建第三方账号或付费服务。
- 不把提示词规范等同于生产护栏，也不把单次模型成功等同于稳定质量。

## License

MIT
