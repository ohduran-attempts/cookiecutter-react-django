# Use an official node runtime as a parent image
FROM node:13.5.0

WORKDIR /app/

# Install dependencies
COPY package.json yarn.lock /app/

# RUN npm install

# Add rest of the client code
COPY . /app/

EXPOSE 3000

CMD npm start