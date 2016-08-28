drop table if exists story;
create table story (
    id integer primary key,
    Story Title text not null,
    User Story text not null,
    Acceptance Criteria text not null,
    Business value integer not null,
    Estimation (h) float
);
