drop table if exists entries;
create table story (
  Story Title text not null,
  User Story text not null,
  Acceptance Criteria text not null,
  Business value text not null,
  Estimation (h) text not null
);
