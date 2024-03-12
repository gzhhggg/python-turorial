import {
  Admin,
  Resource,
  ListGuesser,
} from "react-admin";
import dataProvider from "./dataProvider";
// import simpleRestProvider from "ra-data-simple-rest";
import { ClientList, ClientEdit, ClientCreate } from "./Client";
import { MemberList, MemberEdit, MemberCreate } from "./Member";

const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource
      name="clients"
      list={ClientList}
      recordRepresentation="name"
      edit={ClientEdit}
      create={ClientCreate}
    />
    <Resource
      name="members"
      list={MemberList}
      recordRepresentation="name"
      edit={MemberEdit}
      create={MemberCreate}
    />
    <Resource name="projects" list={ListGuesser} />
  </Admin>
);

export default App;