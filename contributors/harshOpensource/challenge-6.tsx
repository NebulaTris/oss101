import React from "react";

interface Props {
  name: string;
}

const YourGitHubUsername: React.FC<Props> = ({ name }) => {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>This is my TypeScript React component.</p>
    </div>
  );
};

export default YourGitHubUsername;
