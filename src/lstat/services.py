from src.lstat.models import LSTAT_M


async def stat_get_all_by_name(name: str):
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_ = await LSTAT_M.objects.all(LSTAT_M.fl_name == name)
        all_count = len(all_)
        # log.info(f"count load successfuly: {all_count}")
        content = {
            "msg": "Success",
            "count": all_count,
            "data": all_
        }
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {LSTAT_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content


async def stat_get_all():
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_ = await LSTAT_M.objects.all()
        all_count = len(all_)
        # log.info(f"count load successfuly: {all_count}")
        content = {
            "msg": "Success",
            "count": all_count,
            "data": all_
            }
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {LSTAT_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content


async def stat_create_item(item: LSTAT_M):
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_ = await LSTAT_M(**item.dict()).save()
        # all_count = len(all_)
        # log.info(f"count load successfuly: {all_count}")
        content = {
            "msg": "Success",
            "count": 1,
            "data": all_
            }
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {LSTAT_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content

