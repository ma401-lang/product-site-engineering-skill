# Contributing

欢迎提交能提高通用性、可执行性或验证覆盖率的改进。

## 提交原则

- 不提交客户名称、私有提示词、原始对话、访问令牌、生产日志或未授权内容。
- 让 `SKILL.md` 保持短而可路由；详细说明放在 `references/`，重复操作放在 `scripts/`。
- 新增工程规则时，同时说明可执行的验收方式；不要只增加口号。
- 修改工作台模板时，更新审计脚本和测试。
- 与某个框架或供应商相关的规则必须标明适用条件，不得伪装成通用事实。

## 本地检查

```bash
python3 product-site-engineering/scripts/validate_skill.py .
python3 -m unittest discover -s tests -v
```

Pull request 请说明：问题、变更、验证证据、兼容性与仍未解决的限制。
