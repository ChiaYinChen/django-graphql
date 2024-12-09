# Django with Strawberry GraphQL

This project is for practicing integration of Django with Strawberry GraphQL.

## Environment

Python 3.12

- django (5.1.1)
- strawberry-graphql-django (0.48.0)

## Development

- To start the whole stack, run:

  ```
  $ make up
  ```

- To take down the stack, run:

  ```
  $ make down
  ```

- To view logs for a specific service, use `logs-{service}`. You can also customize the number of log lines to display with the `log_lines` argument:

  ```
  $ make logs-api log_lines=50
  ```

## GraphQL Documentation

The GraphQL interface is accessible at [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/). You can use this interface to test API endpoints and explore the schema documentation.
