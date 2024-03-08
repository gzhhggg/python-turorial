import { Admin, Resource, ListGuesser } from "react-admin";
import dataProvider from "./dataProvider";

const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource name="clients" list={ListGuesser} recordRepresentation={"name"} />
    <Resource name="members" list={ListGuesser} recordRepresentation={"name"} />
    <Resource name="projects" list={ListGuesser} />
  </Admin>
);

export default App;