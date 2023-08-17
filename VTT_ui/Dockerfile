FROM node:14

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json for npm install
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application (replace with your actual build command)
RUN npm run build

# Change to a non-root user for running the application
RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
USER nonroot

# Start the application
CMD ["npm", "run", "backend"]