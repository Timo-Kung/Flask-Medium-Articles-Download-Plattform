import urllib.request as req
import json
import pdfkit


def search_content(search):
    url = "https://medium.com/_/graphql"

    requestData = {"operationName": "TagFeedQuery",
                   "variables": {"tagSlug": "data-science", "mode": "HOT", "paging": {"limit": 10}},
                   "query": "query TagFeedQuery($paging: PagingOptions, $tagSlug: String, $mode: TagFeedMode) {\n  tagFeed(paging: $paging, tagSlug: $tagSlug, mode: $mode) {\n    items {\n      ... on TagFeedItem {\n        feedId\n        reason\n        moduleSourceEncoding\n        postProviderExplanation {\n          reason\n          topic {\n            name\n            __typename\n          }\n          __typename\n        }\n        post {\n          ...TagFeedItem_post\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    pagingInfo {\n      next {\n        limit\n        to\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TagFeedItem_post on Post {\n  id\n  title\n  mediumUrl\n  creator {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  firstPublishedAt\n  voters(paging: {limit: 3}) {\n    items {\n      user {\n        ...FacePile_user\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  postResponses {\n    count\n    __typename\n  }\n  allowResponses\n  isLimitedState\n  ...MultiVote_post\n  ...PostPreviewAvatar_post\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostListingReadingTime_post\n  ...PostPresentationTracker_post\n  ...PostFooterSocialPopover_post\n  ...usePostUrl_post\n  __typename\n}\n\nfragment MultiVote_post on Post {\n  id\n  clapCount\n  creator {\n    id\n    ...SusiClickable_user\n    __typename\n  }\n  isPublished\n  ...SusiClickable_post\n  collection {\n    id\n    slug\n    __typename\n  }\n  isLimitedState\n  ...MultiVoteCount_post\n  __typename\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment SusiClickable_user on User {\n  ...SusiContainer_user\n  __typename\n  id\n}\n\nfragment SusiContainer_user on User {\n  ...SignInOptions_user\n  ...SignUpOptions_user\n  __typename\n  id\n}\n\nfragment SignInOptions_user on User {\n  id\n  name\n  __typename\n}\n\nfragment SignUpOptions_user on User {\n  id\n  name\n  __typename\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  id\n  voterCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  name\n  username\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n\nfragment BookmarkButton_post on Post {\n  visibility\n  ...SusiClickable_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        catalogItemIds\n        __typename\n      }\n      predefinedContainingThis {\n        catalogId\n        predefined\n        catalogItemIds\n        __typename\n      }\n      __typename\n    }\n    ...editCatalogItemsMutation_postViewerEdge\n    ...useAddItemToPredefinedCatalog_postViewerEdge\n    __typename\n    id\n  }\n  ...WithToggleInsideCatalog_post\n  __typename\n}\n\nfragment useAddItemToPredefinedCatalog_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    predefinedContainingThis {\n      catalogId\n      version\n      predefined\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment editCatalogItemsMutation_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    catalogsContainingThis(type: LISTS) {\n      catalogId\n      version\n      catalogItemIds\n      __typename\n    }\n    predefinedContainingThis {\n      catalogId\n      predefined\n      version\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WithToggleInsideCatalog_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        __typename\n      }\n      predefinedContainingThis {\n        predefined\n        __typename\n      }\n      __typename\n    }\n    __typename\n    id\n  }\n  __typename\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  ...NewsletterV3EmailToSubscribersMenuItem_post\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  __typename\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerEdge {\n      id\n      isEditor\n      __typename\n    }\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment NewsletterV3EmailToSubscribersMenuItem_post on Post {\n  id\n  creator {\n    id\n    newsletterV3 {\n      id\n      subscribersCount\n      __typename\n    }\n    __typename\n  }\n  isPublishToEmail\n  isNewsletter\n  __typename\n}\n\nfragment FacePile_user on User {\n  __typename\n  id\n  imageId\n  name\n}\n\nfragment PostListingReadingTime_post on Post {\n  readingTime\n  __typename\n  id\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostFooterSocialPopover_post on Post {\n  id\n  mediumUrl\n  title\n  ...SharePostButton_post\n  __typename\n}\n\nfragment SharePostButton_post on Post {\n  id\n  __typename\n}\n\nfragment usePostUrl_post on Post {\n  id\n  creator {\n    id\n    customDomainState {\n      live {\n        domain\n        __typename\n      }\n      __typename\n    }\n    hasSubdomain\n    username\n    __typename\n  }\n  collection {\n    id\n    domain\n    slug\n    __typename\n  }\n  isSeries\n  mediumUrl\n  sequence {\n    slug\n    __typename\n  }\n  uniqueSlug\n  __typename\n}\n"}
    request = req.Request(url, headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }, data=json.dumps(requestData).encode("utf-8"))

    with req.urlopen(request) as response:
        result = response.read().decode("utf-8")

    result = json.loads(result)
    items = result["data"]["tagFeed"]["items"]

    return items


def search_metadata(items, i=1):
    all_items = {}
    for item in items:
        title = item["post"]["title"]
        link = item["post"]["mediumUrl"]
        image = "https://miro.medium.com/fit/c/160/107/" + item["post"]["previewImage"]["id"]
        all_items['{}'.format(i)] = {"title": title, "link": link, "image": image}
        i = i + 1
    return all_items


def download(tit, url):
    confg = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\wkhtmltopdf.exe')
    finish = pdfkit.from_url(url, 'F:\Flask\music_platform\webpage_html\\' + tit + '.pdf', configuration=confg)
    return finish


def page_bar(search):
    others = {
        "2": "/tag/artificial-intelligence?source=topics_v2---------0-----------artificial_intelligence-------28-------------",
        "3": "/tag/data-science?source=topics_v2---------1-----------data_science-------28-------------",
        "4": "/tag/deep-learning?source=topics_v2---------2-----------deep_learning-------28-------------",
        "5": "/tag/python?source=topics_v2---------3-----------python-------28-------------",
        "6": "/tag/ai?source=topics_v2---------4-----------ai-------28-------------",
        "7": "/tag/technology?source=topics_v2---------5-----------technology-------28-------------",
        "8": "/tag/programming?source=topics_v2---------6-----------programming-------28-------------"}
    return others
