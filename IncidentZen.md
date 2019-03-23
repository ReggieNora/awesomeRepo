# Creating incident tickets using Zendesk.

As you all have experienced so far, Zendesk is a powerful new addition to our arsenal of supportocat  tools. There are a few things you maybe wondering how to do, one of those things is incident ticketing.

This is an important tool because it helps us to notify users and organizations if they are doing something that goes outside of our usual allowance.

# It's new and confusing! Gaahhh! How do we start?

You probaly are feeling just like I did when I was trying to figure out how to do this as well. Zendesk is awesome but the buttons can resemble that of a fighter jet if you are trying to do something you remember being easy on Halp and you don't know where to start. Fear not, others have pressed the wrong buttons for you already...

Typically, depending on if there is an owner (or owners) we would have to choose between sending out a bulk ticket or a single ticket. Let's take a look at both methods.

## Bulk tickets!

So, lets just dive into the deep end first! The feeling of danger makes it that much more fun!

Bulk tickets are when you run into the instance where you have more than one owner listed as an owner in StaffTools (Is that camel case?). You can find this information out from the repo in question by searching for it in StaffTools.

## First, We get an issue from Infrastructure!

  - We would get something that looks like this:
    - github/community-and-developer-support#2077

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
Body
https://github.com/github/zendesk/blob/master/canned-replies/Technical/incidents/excessive-resource-usage.md
```

Next, press “Go” to generate the JSON data and then press the “Copy to Clipboard icon” to copy the JSON data.
