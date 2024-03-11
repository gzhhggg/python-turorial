import {
  DatagridConfigurable,
  DateField,
  List,
  SearchInput,
  TextField,
  TopToolbar,
  SelectColumnsButton,
  FilterButton,
  CreateButton,
  ExportButton,
  Pagination,
  Create,
  SimpleForm,
  Edit,
  TextInput,
} from "react-admin";

const ClientPagination = () => (
  <Pagination rowsPerPageOptions={[10, 25, 50, 100]} />
);

const ListActions = () => (
  <TopToolbar>
    <SelectColumnsButton />
    <FilterButton />
    <CreateButton />
    <ExportButton />
  </TopToolbar>
);

const ClientFilters = [
  <SearchInput source="q" alwaysOn />,
];

export const ClientList = () => (
  <List
    actions={<ListActions />}
    filters={ClientFilters}
    pagination={<ClientPagination />}
  >
    <DatagridConfigurable rowClick="edit">
      <TextField source="id" />
      <TextField source="name" />
      <DateField source="created_at" />
      <DateField source="deleted_at" />
    </DatagridConfigurable>
  </List>
);

export const ClientEdit = () => (
  <Edit>
    <SimpleForm>
      <TextField source="id" />
      <TextInput source="name" />
      <DateField source="created_at" />
      <DateField source="deleted_at" />
    </SimpleForm>
  </Edit>
);

export const ClientCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput source="name" />
    </SimpleForm>
  </Create>
);