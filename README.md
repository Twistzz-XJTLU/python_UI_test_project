# Selenium3+Pytest+Allure落地Python Web自动化测试


UI自动化测试使用python3+selenium3+pytest+allure+图像识别实现
1. 通过git clone代码到本地
2. 进入项目目录
3. 安装必要依赖
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 目录介绍
> base: 包括selenium二次封装以及各个页面元素的封装
> 
> common: 包括部分通用方法
> 
> config: 包括driver方法和配置文件
> 
> img: 存放图片
> 
> logs: 日志相关
> 
> page: 页面类
> 
> testcase: 测试用例

## 执行用例
1. 本地运行
```
pytest -s -q testcases
```
2. 放在jenkins运行

