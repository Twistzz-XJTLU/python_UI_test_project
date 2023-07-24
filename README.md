# Selenium3+Pytest+Allure落地Python Web自动化测试

## 项目概述

UI自动化测试使用python3+selenium3+pytest+allure+图像识别实现

![](https://cdn.staticaly.com/gh/Twistzz-XJTLU/picx-images-hosting@master/FireShot-Capture-042---Selenium3+Pytest+Allure落地Python-Web自动化测试---慕课网---coding.imooc.com.4eolp719s460.webp)

## 运行项目

1. 通过git clone代码到本地
2. 进入项目目录
3. 安装必要依赖
```
pip install -r requirements.txt 
```

## 项目结构

- **base**: 存放元素定位和 selenium的二次封装

  - 前面都是单个页面的进行元素定位

    ```
    AccountBase.py
    GoodsBase.py
    HomeBase.py
    IframeBaiduMapBase.py
    IframeImoocBase.py
    LeftMenuBase.py
    LoginBase.py
    OrderBase.py
    TradingMarketBase.py
    ObjectMa.py selenium: 的二次封装  等待完加载完成 等待页面元素消失 等待页面元素出现 跳转地址 元是否显示 元素填值 元素点击 文件上传 iframe相关操作 元素截图 滚动等操作
    ```

- **common package**: 存放通用方法

  - 自动把测试结果发送到钉钉群和企业微信群

  - Jenkins配置

  - MySQL和Redis操作

  - 读取YAML中的数据

- config package: 一些配置项

  - driver_config.py: 对web driver进行了配置
  - environment.yaml: 对用户账号 MySQL Jenkins 等数据进行了存储

- **img package**: 对图片进行了存储 需要图像识别 进行自动化测试

- **logs package** : 日志管理

- **page package**: 存放页面的元素操作 需要继承base中的元素定位和ObjectMap 也就是二次封装

- **testcases package**: 存放测试用例

- **testcase_result.py**: 获取测试测试结果 生成测试报告并自动发送到钉钉和企业微信群

## 页面对象PO模式

把元素定位 元素操作 测试用例 分离开来

<img src="https://cdn.staticaly.com/gh/Twistzz-XJTLU/picx-images-hosting@master/微信图片_20230722172841.gw15aryfahk.webp" style="zoom:67%;" />

<img src="https://cdn.staticaly.com/gh/Twistzz-XJTLU/picx-images-hosting@master/aba1084228dc3928965d72aec64a828.76nnq4tsjcw0.webp" style="zoom: 40%;" />

上图中,当页面元素发生变化 只需要修改 最上面元素定位 user_name 剩下的 元素操作和测试用例都不需要修改 

## 执行用例

1. 本地运行
```
pytest -s -q testcases
```
2. 放在jenkins运行

