import json


class JsonFormatting:

    def __init__(self):
        self.json = {"tools":[{"id":"toc","text":"图层","tooltip":"","enable":1},{"id":"view","text":"地图操作","tooltip":"","enable":1},{"id":"zoomIn","text":"放大","tooltip":"","enable":1},{"id":"zoomOut","text":"缩小","tooltip":"","enable":1},{"id":"clickZoomIn","text":"点击放大","tooltip":"","enable":1},{"id":"clickZoomOut","text":"点击缩小","tooltip":"","enable":1},{"id":"clickCenterAt","text":"点击居中","tooltip":"","enable":1},{"id":"customLocate","text":"自定义范围","tooltip":"","enable":1},{"id":"pan","text":"漫游","tooltip":"","enable":1},{"id":"zoomToFullExtent","text":"全图","tooltip":"","enable":1},{"id":"zoomToPrevExtent","text":"前图","tooltip":"","enable":1},{"id":"zoomToNextExtent","text":"后图","tooltip":"","enable":1},{"id":"tools","text":"工具","tooltip":"","enable":1},{"id":"distanceMeasure","text":"测距","tooltip":"","enable":1},{"id":"areaMeasure","text":"测面","tooltip":"","enable":1},{"id":"print","text":"打印","tooltip":"","enable":1},{"id":"mapSaveAs","text":"地图另存为","tooltip":"","enable":1},{"id":"pipeLineQuery","text":"管线查询","tooltip":"","enable":1},{"id":"identify","text":"快速查询","tooltip":"","enable":1},{"id":"identify","text":"快速查询","tooltip":"","enable":1},{"id":"spatialQuery","text":"空间查询","tooltip":"","enable":2},{"id":"query","text":"管线明细","tooltip":"","enable":2},{"id":"conditionQuery","text":"条件查询","tooltip":"","enable":1},{"id":"pipeStatistic","text":"管线统计","tooltip":"","enable":1},{"id":"pipePointStatistic","text":"管点统计","tooltip":"","enable":1},{"id":"pipeLineStatistic","text":"管线统计","tooltip":"","enable":1},{"id":"spatialStatistic","text":"空间统计","tooltip":"","enable":1},{"id":"fractureAnalysis","text":"断面分析","tooltip":"","enable":1},{"id":"tranSectionAnalysis","text":"横断面分析","tooltip":"","enable":1},{"id":"verticalsectionAnalysis","text":"纵断面分析","tooltip":"","enable":1},{"id":"spatialAnalysis","text":"空间分析","tooltip":"","enable":1},{"id":"pipeBurstAnalysis","text":"爆管分析","tooltip":"","enable":2},{"id":"connectivityAnalysis","text":"连通性分析","tooltip":"","enable":1},{"id":"bufferParamAnalysis","text":"缓冲区分析","tooltip":"","enable":1},{"id":"sectionAnalysis","text":"剖面分析","tooltip":"","enable":1},{"id":"pipeLineCollision","text":"管线碰撞","tooltip":"","enable":1},{"id":"pipeDisTance","text":"间距分析","tooltip":"","enable":1},{"id":"overburdenDepthAnalysis","text":"覆土深度分析","tooltip":"","enable":1},{"id":"crossingAnalysis","text":"交叉口分析","tooltip":"","enable":1},{"id":"parallelDistanceAnalysis","text":"水平净距分析","tooltip":"","enable":2},{"id":"dataUpload","text":"数据上报","tooltip":"","enable":1},{"id":"uploadFile","text":"数据上报","tooltip":"","enable":1},{"id":"uploadFileManage","text":"上报数据处理","tooltip":"","enable":1},{"id":"statUploadData","text":"上报统计","tooltip":"","enable":1},{"id":"uploadDataResult","text":"上报结果","tooltip":"","enable":1},{"id":"polling","text":"管线巡检","tooltip":"","enable":1},{"id":"pollingInfo","text":"巡检信息查看","tooltip":"","enable":1},{"id":"pollingThematic","text":"巡检专题图","tooltip":"","enable":1},{"id":"warning","text":"报废预警","tooltip":"","enable":1},{"id":"emergencyProcessing","text":"应急处理","tooltip":"","enable":1},{"id":"emergencyProcessingInfo","text":"应急信息查看","tooltip":"","enable":1},{"id":"emergencyProcessingThematic","text":"应急专题图","tooltip":"","enable":1},{"id":"accidentStatistic","text":"事故统计分析","tooltip":"","enable":1},{"id":"refreash","text":"刷新","tooltip":"","enable":1}],"groupTools":[["toc",{"id":"view","text":"地图操作","items":["zoomIn","zoomOut","clickZoomIn","clickZoomOut","clickCenterAt","customLocate","pan","zoomToFullExtent","zoomToPrevExtent","zoomToNextExtent"]},{"id":"tools","text":"工具","items":["distanceMeasure","areaMeasure","print","mapSaveAs"]}],[{"id":"pipeLineQuery","text":"管线查询","items":["identify","spatialQuery","query","conditionQuery"]},{"id":"pipeStatistic","text":"管线统计","items":["pipePointStatistic","pipeLineStatistic","spatialStatistic"]}],[{"id":"fractureAnalysis","text":"断面分析","items":["tranSectionAnalysis","verticalsectionAnalysis"]},{"id":"spatialAnalysis","text":"空间分析","items":["pipeBurstAnalysis","valveClosedAnalysis","connectivityAnalysis","bufferParamAnalysis","sectionAnalysis"]},{"id":"pipeLineCollision","text":"管线碰撞","items":["pipeDisTance","overburdenDepthAnalysis","crossingAnalysis","parallelDistanceAnalysis"]}],[{"id":"dataUpload","text":"数据上报","items":["uploadFile","uploadFileManage","statUploadData","uploadDataResult"]}],["refreash"]]}
        self.go()

    def go(self):
        js = json.dumps(self.json)
        print(js)
    