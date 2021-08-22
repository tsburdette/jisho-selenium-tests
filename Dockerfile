FROM python
LABEL maintainer="tsburdette@gmail.com"
COPY . /jisho-selenium-tests
WORKDIR /jisho-selenium-tests
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "--html=report.html"]
CMD tail-f /dev/null