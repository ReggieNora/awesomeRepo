# Creating incident tickets using Zendesk.

As you all have experienced so far, Zendesk is a powerful new addition to our arsenal of supportocat  tools. There are a few things you maybe wondering how to do, one of those things is incident ticketing.

This is an important tool because it helps us to notify users and organizations if they are doing something that goes outside of our usual allowance.

## It's new and confusing! Gaahhh! How do we start?

You probaly are feeling just like I did when I was trying to figure out how to do this as well. Zendesk is awesome but the buttons can resemble that of a fighter jet if you are trying to do something you remember being easy on Halp and you don't know where to start. Fear not, others have pressed the wrong buttons for you already...

Typically, depending on if there is an owner (or owners) we would have to choose between sending out a bulk ticket or a single ticket. Let's take a look at both methods.

## Bulk tickets!

So, lets just dive into the deep end first! The feeling of danger makes it that much more fun!

Bulk tickets are when you run into the instance where you have more than one owner listed as an owner in StaffTools (Is that camel case?). You can find this information out from the repo in question by searching for it in StaffTools.

## First, We get an issue from Infrastructure!

  - We would get something that looks like this:
    - https://github/community-and-developer-support#2077

## Next, we would identify the account type:

  - If this is an org, we would need need the organization-owned repository (name with owner). After that...

## We would use Bulk Ticketer in Stafftools:

  - https://admin.github.com/stafftools/bulk_ticketer

  - “URLs, one per line” - each line should be a formatted URL to a repository

  Example:[https://github.com/owner/repo](https://github.com/owner/repo)

  **Warning callout:** Please use only one repo for the org; specifying N repos will generate N notifications!

In the bulk ticketer, your fields should look something like this:

```
Subject
```
```
From GitHub: SUBJECT_TITLE
```
```
Tags (Omit for now)
```
```
Body should have a reply similar to this link:

https://github.com/github/zendesk/blob/master/canned-replies/Technical/incidents/excessive%20resource%20usage.md
```

Next, press “Go” to generate the JSON data and then press the “Copy to Clipboard icon” to copy the JSON data. Next we move back to Zendesk...

# Open Zendesk to start the bulk ticketing process!

- Go to Zendesk and create a new ticket and fill out the following inputs in left drawer

- Set Requester as `GitHub Staff` - githubstaff@noreply.github.com

- Set Brand as `GitHub Developer Support`

- Set Assignee as `Technical Support`

- Set Form as `Technical Support`

- Set Action as `Incident`

- Set Category as the most relevant one

- Set Type as `Problem`

- Set Subject as something that Supportocats will use internally since the JSON data already includes a pre-populated subject

- Add internal note with link to incident issue

- Submit Ticket as `Open`

  - Ticket must be created. Otherwise, GitHub sidecar won’t appear in Apps Drawer.

- Paste JSON from Bulk Ticketer into an Internal Note
Toggle the Apps draw and click Bulk Ticket Blast in the GitHub Sidecar app

**Warning!** You **must** leave your browser tab open and stay on the page until the tickets are all created -- the tickets are created by your browser talking to the Zendesk API, so if you navigate away before it says it is done, you might not create all of the tickets you were expecting to create.

- Tickets for each owner will be created as Incident tickets and linked to the original Problem ticket

- Submit the Problem ticket as `On-Hold` and Snooze for the desired time period

- Once the incident is resolved, reply to all owners via the Problem ticket and submit as solved ensuring each additional incident ticket is also solved.
---

That's all there is to it for creating bulk tickets for multiple users! Doing this for individual users is a bit easier.

# How to create single tickets for single users in Zendesk!

  - Create a new ticket for that person as a requester

  - In internal comment, link to incident issue

  - Use the excessive resource usage canned reply and send it as Pending.

  As you can see above, the bulk ticketer is not needed to make a single ticket. The steps above should be enough to accomplish your goal.
