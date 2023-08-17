# Use the official Node.js image as the base
FROM node:14

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Expose the port that the Vue.js app will run on
EXPOSE 8082

# Start the development server
CMD ["npm", "run", "serve"]
