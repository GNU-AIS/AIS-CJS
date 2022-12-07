import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 그래프 그리기 1
y = np.arange(29)
years = ['IT기획자',
'IT컨설턴트',
'정보보호컨설턴트',
'업무분석가',
'데이터분석가',
'IT PM',
'IT PMO',
'SW 아키텍트',
'Infrastructure아키텍트',
'데이터 아키텍트',
'UI/UX 개발자',
'UI/UX 디자이너',
'응용SW 개발자',
'시스템SW 개발자',
'임베디드SW 개발자',
'데이터베이스 운용자',
'NW엔지니어',
'IT시스템운용자',
'IT지원 기술자',
'SW제품 기획자',
'IT서비스 기획자',
'IT기술영업',
'IT품질관리자',
'IT테스터',
'IT감리',
'IT감사',
'정보보호관리자',
'침해사고대응전문가',
'IT교육강사'
]
values = [36,48,34,54,32,40,34,44,55,41,27,22,30,23,26,24,33,29,19,38,34,34,42,20,42,23,38,30,27]
colors = ['#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B', '#4EBA5B']

plt.figure(figsize=(15, 10))
plt.xlabel('일 평균 임금(만)')
plt.ylabel('구분')

plt.barh(y, values, color = colors)
plt.yticks(y, years)
plt.savefig('일 평균 임금.png')

# 그래프 그리기 2
y = np.arange(29)

values = [749,1008,722,1140,672,846,718,932,1157,862,570,475,636,496,543,506,698,618,397,798,722,710,883,416,882,492,803,627,580]
colors = ['#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67', '#E8EC67']
plt.figure(figsize=(15, 10))
plt.xlabel('월 평균 임금(만)')
plt.ylabel('구분')

plt.barh(y, values, color = colors)
plt.yticks(y, years)
plt.savefig('월 평균 임금.png')

# 그래프 그리기 3
y = np.arange(29)

values = [45038,60592,43390,68569,40398,50853,43179,56030,69564,51846,34308,28590,38254,29848,32661,30411,41997,37148,23883,47999,43414,42709,53098,25017,53060,29610,48264,37685,34896]
colors = ['#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6', '#4e79a6']
plt.figure(figsize=(15, 10))
plt.xlabel('시간 평균 임금(원)')
plt.ylabel('구분')

plt.barh(y, values, color = colors)
plt.yticks(y, years)
plt.savefig('시간평균 임금.png')

plt.show()

