"""
MVC 패턴

Model: DTO (data transfer object) + DAO (data access object)
Service: Business Login (Algorithm)
Controller: RESTful 방식으로 React Axios 로 통신

모델-뷰-컨트롤러 패턴 (Model-view-controller pattern)
MVC 패턴이라고도 하는 이 패턴은 대화형 애플리케이션 (interactive application)을 다음의 3 부분으로 나눈다.

모델 (model) — 핵심 기능과 데이터를 포함한다
          - Service, Model
                     - DTO, DAO -> orm
          - Model (*.py memory): Machine (*.h5 disk) 저장된 형태
          - Service : 저장된 모델을 호출하여 기능을 수행하게 하는 파트
뷰 (view) — 사용자에게 정보를 표시한다 (하나 이상의 뷰가 정의될 수 있음)
컨트롤러 (controller) — UI 로부터의 입출력을 처리한다


AI-Calc 에서 사칙연산을 나누는 이유
머신 model-* 은 history 를 기억하는 능력이 있습니다.
5 + 2 = 7 
5 + * = *

....

5 덧셈연산을 제안 ...
7 * ....
7 곱셈연산을 제안 ...


텐서에서 변수의 저장은 확률변수

0 0 0 0 8.0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0 

Java 
float a = 8.0


"""