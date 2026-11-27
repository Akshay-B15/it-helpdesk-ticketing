## Permission Matrix

| Action                        | Employee | Agent | Admin | Notes                                                                                                                                                                                                  |
| ----------------------------- | -------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create tickets                | ✅        | ❌     | ❌     | Employees will have the access to create the ticket after logging in                                                                                                                                   |
| View own tickets              | ✅        | N/A   | N/A   | Employees can only view the tickets created by them                                                                                                                                                    |
| View assigned tickets         | N/A      | ✅     | N/A   | Agents can only view the tickets assigned to them                                                                                                                                                      |
| View unassigned tickets       | ❌        | ❌     | ✅     | Only Admins will have access to view unassigned tickets                                                                                                                                                |
| View all tickets              | ❌        | ❌     | ✅     | Only Admins can view all the tickets                                                                                                                                                                   |
| Edit title/description        | ✅        | ❌     | ❌     | Only employees can edit the title and description field of their own tickets only when it is in open status                                                                                            |
| Change priority               | ❌        | ❌     | ✅     | Only Admins can change the priority                                                                                                                                                                    |
| Assign ticket to agent        | ❌        | ❌     | ✅     | Only Admins can assign the tickets to agents                                                                                                                                                           |
| Set In Progress               | ❌        | ✅     | ❌     | Only Agents can set the status field to 'In Progress' for assigned tickets, ticket will stay in open status until the agent changes it to 'In Progress'                                                |
| Set Resolved                  | ❌        | ✅     | ❌     | Only Agents can set the status field to 'Resolved' for assigned tickets                                                                                                                                |
| Edit resolution notes         | ❌        | ✅     | ❌     | Only Agents can edit resolution notes to assigned tickets                                                                                                                                              |
| View resolution notes         | ✅        | ✅     | ✅     | Employees can view the resolution notes of their own ticket, Agents can view the resolution notes of the tickets that were assigned to them, Admin can view resolution notes for all tickets           |
| Approve closure               | ✅        | ❌     | ❌     | Only employees can approve their own ticket to be closed once the status is set to resolved                                                                                                            |
| Reopen ticket                 | ✅        | ❌     | ❌     | Only employees can reopen their own ticket once the ticket is set to resolved                                                                                                                          |  |
| Create / manage user accounts | ❌        | ❌     | ✅     | Only Admins can create and manage the user accounts                                                                                                                                                    |
| Delete duplicate tickets      | ❌        | ❌     | ✅     | The systems cannot check if the tickets are duplicate, therefore Admins can delete any tickets and limiting it to duplicates is a policy. Every deletion is logged so that the admins stay accountable |


## Transition list:

The following shows the transition of the ticket's status from open to closed. The ticket status is set to open once the ticket is created by the employee. The ticket's status can not be changed once the status is set to closed.

- Open --> In Progress (Set by the agent)
- In Progress --> Resolved (Set by the agent)
- Resolved --> Closed (Set by the employee once the employee approve the closure request)
- Resolved --> Open (Set by the employee if the ticket is reopened and it stays assigned to the same agent)