import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
font_path="korean.ttf" ##그래프에서 한글 오류가 안나게하는 폰트
font_name=font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

Sc = pd.read_csv("open.csv",encoding='cp949')

Sc.dtypes

print(Sc)
##시설과 면적의 평균과 오름차순 내림차순으로 정렬
print("체육시설 지역 평균 수")
print(Sc["시설수"].mean())
print("===============================================================")
print("시설이 많은 지역 순으로")
print(Sc.sort_values(by=['시설수'], ascending=False).head(18))
print("===============================================================")
print("면적이 넓은 순으로")
print(Sc.sort_values(by=['면적'], ascending = False).head(18))
print("===============================================================")
print("시설이 적은 지역 순으로")
print(Sc.sort_values(by=['시설수'], ascending = True).head(18))
print("===============================================================")
print("면적이 적은 지역 순으로")
print(Sc.sort_values(by=['면적'], ascending = True).head(18))

Sc.plot(kind='bar',x='지역',y='시설수', color='blue') ##지역별 체육시설 분포 그래프
plt.show()
