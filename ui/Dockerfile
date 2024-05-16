# pull official base image
FROM node:20.13.1-alpine3.19

# set working directory
WORKDIR /app

COPY . .

RUN apk add --no-cache curl
RUN npm install

EXPOSE 3000

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# start app
CMD ["npm", "start"]