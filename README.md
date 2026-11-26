# 벤치마크 조회 (설치형 웹앱)

신약 밸류에이션 벤치마크 통계(성공확률, 소요기간, 딜 구조, 시장점유율)를 검색하고 출처와 함께 확인하는 정적 웹앱입니다. 서버와 빌드 과정이 없습니다.

## 구성
- index.html: 화면과 검색 로직
- data.js: 벤치마크DB(stats, metrics, sources)를 변환한 데이터
- sw.js, manifest.webmanifest, icon-*.png: 오프라인 동작과 홈 화면 설치
- gen_data.py: 벤치마크DB 폴더의 CSV 3종에서 data.js를 다시 만드는 스크립트

## 데이터 갱신
    python gen_data.py <벤치마크DB 폴더> data.js
sw.js의 V 값(예: bench-v1-20261126)을 올려야 설치된 앱이 새 데이터를 받습니다.

## 포함하지 않는 것
원문 PDF는 포함하지 않으며 DOI와 PubMed 링크로만 연결합니다.
